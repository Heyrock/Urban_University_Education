from pprint import pprint
import requests
import inspect
import sys

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


# pprint(dir(sys))

# Путь к интерпретатору Пайтон
"""print(sys.executable)"""
# C:\Users\Ром\Documents\Urban_1\venv\Scripts\python.exe

# ----------------------------------

# В какой операционной системе работаем
"""print(sys.platform)"""
# win32

# ----------------------------------

# Текущая версия Python
"""print(sys.version)"""
# 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
"""print(sys.version_info)"""
# sys.version_info(major=3, minor=11, micro=2, releaselevel='final', serial=0)

# ----------------------------------

# Список, содержащий параметры командной строки, если она была задана
"""print(sys.argv)"""
# ['C:\\Users\\Ром\\Documents\\Urban_1\\Urban_lectures\\_11_4_introspection_3.py']

# ----------------------------------

# Путь поиска модуля, список каталогов, в которых Python будет искать модули во время импорта
"""pprint(sys.path)"""
# ['C:\\Users\\Ром\\Documents\\Urban_1\\Urban_lectures',
#  'C:\\Users\\Ром\\Documents\\Urban_1',
#  'C:\\Python311\\python311.zip',
#  'C:\\Python311\\DLLs',
#  'C:\\Python311\\Lib',
#  'C:\\Python311',
#  'C:\\Users\\Ром\\Documents\\Urban_1\\venv',
#  'C:\\Users\\Ром\\Documents\\Urban_1\\venv\\Lib\\site-packages']

# ----------------------------------

# Словарь, который отображает имена модулей в объектах модулей для всех,
# загруженных в текущий момент модулей
"""pprint(sys.modules)"""
# {'__future__': <module '__future__' from 'C:\\Python311\\Lib\\__future__.py'>,
#  '__main__': <module '__main__' from 'C:\\Users\\Ром\\Documents\\Urban_1\\Urban_lectures\\_11_4_introspection_3.py'>,
#  '_abc': <module '_abc' (built-in)>,
#  '_ast': <module '_ast' (built-in)>,
#  '_bisect': <module '_bisect' (built-in)>,
# ...}

# ----------------------------------

# Псевдо-модуль __builtins__ - содержащий встроенные в интерпретатор объекты:
# (константы, исключения, функции)
"""print(__builtins__)"""
# <module 'builtins' (built-in)>
"""pprint(dir(__builtins__))"""
# ['ArithmeticError',
#  'AssertionError',
#  'AttributeError',
#  'BaseException',
#  ...]

# ----------------------------------

"""def func(x):
    try:
        if sys.version.split(' ')[0] == '3.11.3':
            return x + 10
        else:
            raise Exception('Недопустимая версия')
    except Exception as e:
        print(e.args)

print(func(3))"""

# ----------------------------------

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(10000)
"""print(factorial(2000))"""
# огромное число
print(sys.getsizeof(factorial))
# 152
