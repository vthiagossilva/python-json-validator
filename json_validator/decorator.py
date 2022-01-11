from asyncio import iscoroutine
from functools import wraps

from json_validator.validate_schema import __validate_schema


def validate_schema(
        schema: dict,
        key: str = "data",
        is_new: bool = True,
        result_type: str = int,
):
    def real_decorator(f):
        @wraps(f)
        async def wrapper(*a, **kw):
            r, s = __validate_schema(kw[key], schema, is_new, result_type)
            if s not in (True, 200):
                return r, s
            return await f(*a, **kw)

        return wrapper
    return real_decorator
