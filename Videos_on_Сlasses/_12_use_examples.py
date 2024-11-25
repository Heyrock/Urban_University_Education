# замена замыканий функций
# здесь функция, удаляющая в конце и начале строки определенные символы
import math


class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        else:
            return args[0].strip(self.chars)


# s1 = StripChars('?!:;. ')
# s2 = StripChars(' ')
# print(s1(' !Hello world?. '))
# print(s2(' !Hello world?. '))
# Hello world
# !Hello world?.



# реализация декораторов
# вычисление производных функции в точке х
class Derivate:
    def __init__(self, func):
        self.func = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.func(x + dx) - self.func(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


# вызов функции без декоратора
print(df_sin(math.pi/3))
# 0.8660254037844386

# вызов функции с классом-декоратором
# df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))
# 0.4999566978958203
