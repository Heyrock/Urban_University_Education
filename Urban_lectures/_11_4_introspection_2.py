from pprint import pprint
import requests
import inspect

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param2 = 'n/a'):
    print('my params are', param, param2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


rename_func = some_function

some_object = SomeClass()

# 4.	Проверить наличие атрибута у объекта
# Функция hasattr()

attr_name = 'attribute_2'
print(hasattr(some_object, attr_name))
# False
print(hasattr(some_object, 'attribute_1'))
# True
pprint(dir(some_object)[-2])
# 'attribute_1'

# -------------------------------------
# 5.	Получить значение атрибута объекта
# Функция getattr().

print(getattr(some_object, 'attribute_1'))
# 27
print(getattr(some_object, dir(some_object)[-2]))
# 27
# print(help(getattr))
print(getattr(some_object, 'attribute_2', None))
# None

# for attr_name in dir(requests):
#     # attr = getattr(requests, attr_name)
#     print(attr_name, type(attr_name))

# -------------------------------------
# 6.	Узнать, можно ли вызывать объект
# Функция callable().

print(callable(some_string))
# False
print(callable(some_function))
# True
print(callable(some_object.attribute_1))
# False
print(callable(some_object.some_class_method))
# True
print(callable(SomeClass))
# True
print()

# -------------------------------------
# 7.	Узнать, является ли определенный объект экземпляром указанного класса
# Функция isinstance().

print(isinstance(some_number, str))
# False
print(isinstance(some_number, int))
# True
print(isinstance(some_number, SomeClass))
# False
print(isinstance(some_object, SomeClass))
# True

# -------------------------------------
# 8.	Модуль inspect для интроспекции
# https://docs.python.org/3/library/inspect.html
# Этот модуль собирает у себя удобные методы и классы для отображения интроспективной информации

print(inspect.ismodule(requests))
# True
print(inspect.isclass(requests))
# False
print(inspect.isfunction(requests))
# False
print(inspect.isbuiltin(requests))
# False

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)
# <class 'module'>
# <module '__main__' from 'C:\\Users\\Ром\\Documents\\Urban_1\\Urban_lectures\\temp_lecture.py'>