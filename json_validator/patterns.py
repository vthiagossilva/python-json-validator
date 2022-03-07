from typing import Iterable


def sigla(digits = 2):
    return {
        "type": str,
        "message": "deve ser <String> no modelo /^[a-zA-Z]{" + str(digits) + "}$/",
        "regex": "^[a-zA-Z]{" + str(digits) + "}$",
        "upper": True
    }


def moment(action = None, default = None, optional: bool = False):
    return {
        "type": str,
        "regex": r"^20[1-2][0-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) [0-5][0-9]:[0-5][0-9]$",
        "message": "deve ser <String> no formato AAAA-MM-DD hh:mm",
        "moment_format": "%Y-%m-%d %H:%M",
        "action": action,
        "default": default,
        "optional": optional,
    }


def date(action = None, default = None, optional: bool = False):
    return {
        "type": str,
        "regex": r"^20[1-2][0-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) [0-5][0-9]:[0-5][0-9]$",
        "message": "deve ser <String> no formato AAAA-MM-DD hh:mm",
        "moment_format": "%Y-%m-%d %H:%M",
        "action": action,
        "default": default,
        "optional": optional,
    }


def regex(r: str, optional: bool = False):
    return {
        "type": str,
        "message": f"deve ser <String> no modelo /{r}/",
        "regex": r,
        "optional": optional
    }


def value(optional: bool = False, only_int: bool = False, action = None, default = None):
    return {
        "type": int if only_int else (float, int),
        "optional": optional,
        "message": f"deve ser <{'Integer' if only_int else 'Float|Integer'}>",
        "action": action,
        "default": default,
    }


def string(min_len: int = 1, max_len: int = None, optional: bool = False, action = None, default = None):
    return {
        "type": str,
        "min_len": min_len,
        "max_len": max_len,
        "optional": optional,
        "message": f"deve ser <String> entre {min_len} e {max_len} caracteres",
        "action": action,
        "default": default,
    }


def choices(choices: Iterable, optional: bool = False, type_choice: tuple = None, action = None, default = None):
    if type_choice is None:
        type_choice = type(choices[0]), str(type(choices[0]))
    else:
        assert isinstance(type_choice, tuple)
        assert len(type_choice) == 2

    return {
        "type": type_choice[0],
        "choices": choices,
        "optional": optional,
        "message": f"deve ser {type_choice[1]} entre: {', '.join(choices)}",
        "action": action,
        "default": default,
    }


def boolean(optional: bool = False):
    return {
        "type": bool,
        "optional": optional,
        "message": "deve ser Boolean"
    }


def digits(interval: str, optional: bool = False, action = None, default = None):
    return {
        "type": str,
        "optional": optional,
        "regex": "^[0-9]{" + interval + "}$",
        "message": "deve ser String no modelo /^[0-9]{" + interval + "}$/",
        "action": action,
        "default": default,
    }


def important(type: str, optional: bool = False, action = None, default = None):
    return {
        "type": str,
        "important": type,
        "optional": optional,
        "action": action,
        "default": default,
    }


def schema(s: dict, name: str, is_list: bool = False, optional: bool = False):
    return {
        "type": list if is_list else dict,
        "optional": optional,
        "schema": s,
        "name": name,
        "message": f"deve ser <Object> seguindo o schema {name}",
    }


def email(optional: bool = False):
    return regex(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", optional=optional)


def nickname(optional: bool = False):
    return regex(r"^(?!\d)(?!.*-.*-)(?!.*-$)(?!-)[a-zA-Z0-9-]{6,20}$", optional=optional)
