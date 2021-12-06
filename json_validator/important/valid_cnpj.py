import re

from json_validator.exceptions import ValidationError


def valid_cnpj(cnpj: str):
    if not isinstance(cnpj, str):
        raise ValidationError("Deve ser uma <String> no formato /^[0-9]{14}$/")
    if not re.match("^[0-9]{14}$", cnpj):
        raise ValidationError("Deve ser uma <String> no formato /^[0-9]{14}$/")

    like_digits = [int(d) for d in cnpj]

    i = 5
    acumulator = 0
    for digit in like_digits[:12]:
        acumulator += digit * i
        if i != 2:
            i -= 1
        else:
            i = 9

    remainder = acumulator % 11
    remainder = 0 if remainder < 2 else 11 - remainder

    if remainder != like_digits[-2]:
        raise ValidationError("Dígito verificador")

    i = 6
    acumulator = 0
    for digit in like_digits[:13]:
        acumulator += digit * i
        if i != 2:
            i -= 1
        else:
            i = 9

    remainder = acumulator % 11
    remainder = 0 if remainder < 2 else 11 - remainder

    if remainder != like_digits[-1]:
        raise ValidationError("Dígito verificador")
