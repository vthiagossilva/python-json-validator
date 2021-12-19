def sigla(digits = 2):
    return {
        "type": str,
        "message": "deve ser <String> no modelo /^[a-zA-Z]{" + str(digits) + "}$/",
        "regex": "^[a-zA-Z]{" + str(digits) + "}$",
        "upper": True
    }


def momento():
    return {
        "type": str,
        "regex": r"^20[1-2][0-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) [0-5][0-9]:[0-5][0-9]$",
        "message": "deve ser <String> no formato AAAA-MM-DD hh:mm",
        "moment_format": "%Y-%m-%d %H:%M"
    }


def data(optional: bool = False):
    return {
        "type": str,
        "regex": r"^20[1-2][0-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) [0-5][0-9]:[0-5][0-9]$",
        "message": "deve ser <String> no formato AAAA-MM-DD hh:mm",
        "moment_format": "%Y-%m-%d %H:%M",
        "optional": optional,
    }


def regex(r: str, optional: bool = False):
    return {
        "type": str,
        "message": f"deve ser <String> no modelo /{r}/",
        "regex": r,
        "optional": optional
    }


def value(optional: bool = False, only_int: bool = False):
    return {
        "type": int if only_int else (float, int),
        "optional": optional,
        "message": f"deve ser <{'Integer' if only_int else 'Float|Integer'}>"
    }


def text(min_len: int = 2, max_len: int = None, optional: bool = False):
    return {
        "type": str,
        "min_len": min_len,
        "max_len": max_len,
        "optional": optional,
        "message": f"deve ser <String> entre {min_len} e {max_len} caracteres"
    }


def choices(choices: list, optional: bool = False, upper: bool = False, type_choice: tuple = None):
    if type_choice is None:
        type_choice = type(choices[0]), str(type(choices[0]))
    else:
        assert isinstance(type_choice, tuple)
        assert len(type_choice) == 2

    return {
        "type": type_choice[0],
        "choices": choices,
        "upper": upper,
        "optional": optional,
        "message": f"deve ser {type_choice[1]} entre: {', '.join(choices)}"
    }


def boolean(optional: bool = False):
    return {
        "type": bool,
        "optional": optional,
        "message": "deve ser Boolean"
    }


def digits(interval: str, optional: bool = False):
    return {
        "type": str,
        "optional": optional,
        "regex": "^[0-9]{" + interval + "}$",
        "message": "deve ser String no modelo /^[0-9]{" + interval + "}$/"
    }


def important(type: str, optional: bool = False):
    return {
        "type": str,
        "important": type,
        "optional": optional,
    }


def schema(s: dict, name: str, is_list: bool = False, optional: bool = False):
    return {
        "type": list if is_list else dict,
        "optional": optional,
        "schema": s,
        "name": name,
        "message": f"deve ser <Object> seguindo o schema {name}",
    }
