from datetime import datetime


def valid_birthday(birth: str) -> datetime:
    if not isinstance(birth, str):
        raise ValueError("É necessário ser uma String no formato AAAA-MM-DD")

    try:
        new_date = datetime.strptime(birth, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Formato incorreto - uma String no formato AAAA-MM-DD era esperada")

    now = datetime.now()
    _18_years_old = datetime(now.year - 18, now.month, now.day)
    _100_years_old = datetime(now.year - 100, now.month, now.day)

    if _18_years_old < new_date:
        raise ValueError("É necessário ter mais de 18 anos")

    if new_date <= _100_years_old:
        raise ValueError("Data acima de 100 anos não permitida")

    return new_date
