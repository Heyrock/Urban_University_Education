# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа)
# в качестве аргумента и проводит интроспекцию этого объекта,
# чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения
# информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую
# информацию:
# - Тип объекта.
# - Атрибуты объекта.
# - Методы объекта.
# - Модуль, к которому объект принадлежит.
# - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...],
# 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания
# Файл с кодом прикрепите к домашнему заданию.

import inspect
from pprint import pprint
import re


def get_type(obj):
    string = str(type(obj))
    pattern_1 = re.compile("<class '")
    pattern_2 = re.compile("'>")
    for i in (pattern_1, pattern_2):
        string = i.sub('', string)
    return string


def get_attr(obj):
    try:
        return [attr for attr in dict(obj.__dict__)]
    except AttributeError:
        return ['None']


def get_methods(obj):
    return [i for i in dir(obj) if i not in get_attr(obj) and '__' not in i]


def get_module(obj):
    return inspect.getmodule(obj)


def introspection_info(obj):
    results = {}
    results['type'] = get_type(obj)
    results['attributes'] = get_attr(obj)
    results['methods'] = get_methods(obj)
    results['module'] = get_module(obj)
    return results


class TestClass:
    def __init__(self):
        self.attr1 = 'Hello'
        self.attr2 = 'World'

    def do_sth(self):
        print('do sth')


instance = TestClass()
instance_info = introspection_info(instance)
pprint(instance_info)

number_info = introspection_info(42)
pprint(number_info)

# {'attributes': ['attr1', 'attr2'],
#  'methods': ['do_sth'],
#  'module': <module '__main__' from 'C:\\Users\\Ром\\Documents\\Urban_1\\Homework\\temp_HW.py'>,
#  'type': '__main__.TestClass'}
#
# {'attributes': ['None'],
#  'methods': ['as_integer_ratio',
#              'bit_count',
#              'bit_length',
#              'conjugate',
#              'denominator',
#              'from_bytes',
#              'imag',
#              'numerator',
#              'real',
#              'to_bytes'],
#  'module': None,
#  'type': 'int'}