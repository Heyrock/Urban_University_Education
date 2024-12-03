# пример 1 - lambda-функции

my_func = lambda x: x + 10

print(my_func(42))
# 52
print(type(my_func))
# <class 'function'>

my_numbers = [3, 1, 4, 3, 5, 6, 7]
result = map(lambda x: x + 10, my_numbers)
print(result)
# <map object at 0x000002408F18BB50>
print(list(result))
# [13, 11, 14, 13, 15, 16, 17]


# пример 2 - У лямбды может быть неограниченное количество аргументов, в том числе ни одного

nums_1 = [3, 1, 4, 3, 5, 6, 7]
nums_2 = [0, 9, 8, 7, 6, 5, 4]

result = map(lambda x, y: x + y, nums_1, nums_2)
print(result)
# [3, 10, 12, 10, 11, 11, 11]


def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2

    elif n == 3:
        def multiplier(x):
            return x * 3

    else:
        raise Exception('Я могу множить только на 2 или 3')

    return multiplier


my_numbers = [1, 2, 3, 4, 5, 6]

by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)

print(list(map(by_2, my_numbers)))
# [2, 4, 6, 8, 10, 12]
print(list(map(by_3, my_numbers)))
# [3, 6, 9, 12, 15, 18]

try:
    by_4 = get_multiplier_v1(4)
    print(list(map(by_4, my_numbers)))
except Exception as exc:
    print(exc)
# Я могу множить только на 2 или 3


def get_multiplier_v1(n):
    def multiplier(x):
        return x * n
    return multiplier


by_5 = get_multiplier_v1(5)
print(by_5(42)) # 210
print(get_multiplier_v1(5)(42)) # 210

my_numbers = [1, 2, 3, 4, 5, 6]

by_10 = get_multiplier_v1(10)
by_100 = get_multiplier_v1(100)

print(list(map(by_10, my_numbers)))
print(list(map(by_100, my_numbers)))


# пример 5 - Не стоит передавать в аргументы функций изменяемые объекты и замыкать их.
from pprint import pprint

def matrix(some_list):
    def multiply_column(x):
        res = []
        for elem in some_list:
            res.append(elem * x)
        return res
    return multiply_column

n1 = [1, 2, 3]
n2 = [6, 7, 8]

matrix1 = matrix(n1)
pprint(list(map(matrix1, n2)))
# [[6, 12, 18], [7, 14, 21], [8, 16, 24]]

n1.extend([10])
pprint(list(map(matrix1, n2)))
# [[6, 12, 18, 60], [7, 14, 21, 70], [8, 16, 24, 80]]


# Пример 6: Создание вызываемого экземпляра класса
class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        # если у класса есть такой метод, то его можно вызывать как функцию
        return self.n * x


nums = [1, 2, 3]
by_100500 = Multiplier(100500)
result = by_100500(42)
print(result)
# 4221000

# print(Multiplier(100500)(42))
# 4221000

print(list(map(by_100500, nums)))
# [100500, 201000, 301500]
