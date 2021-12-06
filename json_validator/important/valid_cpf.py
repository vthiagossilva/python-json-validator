import re


def valid_cpf(cpf: str):
    if not isinstance(cpf, str):
        raise ValueError("Deve ser uma <String> no formato /[0-9]{11}/")
    if not re.match("^[0-9]{11}$", cpf):
        raise ValueError("Deve ser uma <String> no formato /^[0-9]{11}$/")

    check_if_digits_is_equal = [i for i in cpf if i == cpf[0]]
    if len(check_if_digits_is_equal) == len(cpf):
        raise ValueError("Caracteres repetidos")

    like_digits = [int(d) for d in cpf]

    i = 10
    acumulator = 0
    for digit in like_digits[:9]:
        acumulator += digit * i
        i -= 1
    acumulator *= 10
    remainder = acumulator % 11
    remainder = remainder if remainder != 10 else 0

    if remainder != like_digits[-2]:
        raise ValueError("Dígito verificador")

    i = 11
    acumulator = 0
    for digit in like_digits[:10]:
        acumulator += digit * i
        i -= 1
    acumulator *= 10
    remainder = acumulator % 11
    remainder = remainder if remainder != 10 else 0

    if remainder != like_digits[-1]:
        raise ValueError("Dígito verificador")
