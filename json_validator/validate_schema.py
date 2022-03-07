import re
from datetime import datetime
from typing import Any

from json_validator.exceptions import ValidationError
from json_validator.important import valid_cnpj
from json_validator.important import valid_cpf


def __validate_schema(
        data: dict,
        Schema: dict,
        is_new: bool = True,
        result_type = int
) -> (dict, Any):
    assert result_type in (int, bool)

    try:
        if not isinstance(data, dict):
            raise ValidationError('Um Object seguindo o schema apropriado era esperado')

        if is_new:
            for (key, schema) in Schema.items():
                if not schema.get("optional"):
                    if key not in data.keys() and not schema.get("default"):
                        raise ValidationError(f'"{key}" é requerido')
                    elif schema.get("default"):
                        data[key] = schema["default"]

        for (key, value) in data.items():
            try:
                schema = Schema[key]
            except KeyError:
                raise ValidationError(f'"{key}" não existe no schema')

            if not isinstance(value, schema["type"]) or (
                schema.get("choices") and value not in schema["choices"]
            ):
                raise ValidationError(f'"{key}" {schema["message"]}')

            if schema["type"] is str:
                value = value.strip()

                if schema.get("important") == "cnpj":
                    try:
                        valid_cnpj(value)
                    except ValidationError as err:
                        raise ValidationError(f'\"{key}\": ' + err.__str__())
                elif schema.get("important") == "cpf":
                    try:
                        valid_cpf(value)
                    except ValidationError as err:
                        raise ValidationError(f'\"{key}\": ' + err.__str__())
                else:
                    if schema.get("upper"): value = value.upper()
                    data[key] = value

                    if schema.get("regex") and not re.match(schema["regex"], value):
                        raise ValidationError(f'"{key}" {schema["message"]}')

                    if not (schema.get("min_len") or 0) <= len(value) <= (schema.get("max_len") or 5000):
                        raise ValidationError(f'"{key}" {schema["message"]}')

                    if schema.get("moment_format"):
                        try:
                            datetime.strptime(value, schema["moment_format"])
                        except ValidationError as err:
                            print(err)
                            raise ValidationError(f'"{key}" não é um momento válido')

            elif schema["type"] == (float, int):
                if value < 0 and not schema.get("can_negative"):
                    raise ValidationError(f'"{key}" não permite valores negativos')

            elif schema["type"] == list:
                if not value: raise ValidationError(f'"{key}" precisa ter ao menos um elemento')

                for item in value:
                    result, s_code = __validate_schema(item, schema["schema"], is_new)
                    if s_code != 200:
                        return result, s_code

            elif schema["type"] == dict:
                result, s_code = __validate_schema(value, schema["schema"], is_new)
                if s_code != 200:
                    return result, s_code

            if schema.get("action"):
                func = schema["action"]
                data[key] = func(data[key])

        return data, result_type == bool or 200
    except ValidationError as err:
        return {"error": err.__str__()}, False if result_type == bool else 422
