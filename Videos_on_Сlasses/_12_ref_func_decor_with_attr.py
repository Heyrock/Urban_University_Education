# функция-декоратор для сравнения с классом-декоратором
import math
from functools import wraps


def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper
    return func_decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


# классическая запись
# f = df_decorator(0.001)
# sin_df = f(sin_df)
# df = sin_df(math.pi / 3)
# print(df)

# сокращенная запись
# sin_df = df_decorator(0.001)(sin_df)
# df = sin_df(math.pi / 3)
# print(df)

# @-вариант
df = sin_df(math.pi / 3)
print(df)

print(sin_df.__name__)
print(sin_df.__doc__)