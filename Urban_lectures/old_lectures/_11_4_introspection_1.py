# встроенная помощь
from pprint import pprint

import requests
help(requests)
help(requests.get)

# --------------------------
import requests

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param2 = 'n/a'):
    print('my params are', param, param2)


class SomeClass:
    def __init__(self):
        self.attribute1 = 27

    def some_class_method(self, value):
        self.attribute1 = value
        print(self.attribute1)


rename_func = some_function

some_object = SomeClass()

# Пример 1 - Атрибут класса __name__

print(some_function.__name__)
# some_function
print(SomeClass.__name__)
# SomeClass
print(requests.__name__)
# requests
print(some_function.__name__)
# some_function
print(rename_func.__name__)
# some_function

print(some_string.__name__)
# Error
print(some_number.__name__)
# Error
print(some_object.__name__)
# Error

# --------------------------
# Пример 2 - Функция type - Узнаем тип объекта
print(type(some_number))
# <class 'int'>
print(type(some_number) is int)
# True
print(type(some_number) is list)
# False

print(type(requests))
# <class 'module'>


# --------------------------
# Пример 3 - Функция dir()
# Возвращает отсортированный список атрибутов и методов,
# доступных для указанного объекта,
# который может быть объявленной переменной или функцией.

pprint(dir(some_number))
pprint(dir(some_list))
pprint(dir(some_function))
pprint(dir(SomeClass))
pprint(dir(some_object))
pprint(dir(requests))

# без указания аргумента dir() выводит доступные в локальной зоне видимости
pprint(dir())

# --------------------------

# --------------------------