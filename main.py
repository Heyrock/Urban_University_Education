# Задание 10
# Напишите декоратор, который будет измерять производительность функций,
# создающих список с помощью этих методов:
#
# range()
# списковое включение
# append()
# конкатенация
# Среди показателей должны быть:
#
# Время работы функции.
# Текущее потребление памяти.
# Пиковое потребление памяти.
#

import tracemalloc
from time import perf_counter
from functools import wraps
import inspect


def time_memory_used(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start = perf_counter()
        result = function(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        stop = perf_counter()
        print(f'Название функции: {function.__name__}')
        print(f'Использованный метод: {function.__doc__}')
        print(f'Текущее потребление памяти: {current / 10**6:.6f} мб \n'
              f'Пик использования памяти: {peak / 10**6:.6f} мб ')
        print(f'Операция заняла: {stop - start:.6f} секунд')
        tracemalloc.stop()
        return result
    return wrapper


@time_memory_used
def make_list_with_range():
    'range()'
    my_list = list(range(100000))
    # print(inspect.stack()) # Интересненько
    return f'Функция {inspect.stack()[0][3]} завершила работу \n{"-" * 48}'

@time_memory_used
def make_list_comprehension():
    'list comprehension'
    my_list = [l for l in range(100000)]
    return f'Функция {inspect.stack()[0][3]} завершила работу \n{"-" * 48}'


@time_memory_used
def make_list_with_append():
    'append()'
    my_list = []
    for item in range(100000):
        my_list.append(item)
    return f'Функция {inspect.stack()[0][3]} завершила работу \n{"-" * 48}'


@time_memory_used
def make_list_concatenation():
    'конкатенация'
    my_list = []
    for item in range(100000):
        my_list = my_list + [item]
    return f'Функция {inspect.stack()[0][3]} завершила работу \n{"-" * 48}'


# print(make_list_with_range())
# print(make_list_comprehension())
# print(make_list_with_append())
# print(make_list_concatenation())
#
# Название функции: make_list_with_range
# Использованный метод: range()
# Текущее потребление памяти: 0.034127 мб
# Пик использования памяти: 4.038928 мб
# Операция заняла: 0.092711 секунд
# Функция make_list_with_range завершила работу
# ------------------------------------------------
# Название функции: make_list_comprehension
# Использованный метод: list comprehension
# Текущее потребление памяти: 0.000526 мб
# Пик использования памяти: 3.994862 мб
# Операция заняла: 0.067124 секунд
# Функция make_list_comprehension завершила работу
# ------------------------------------------------
# Название функции: make_list_with_append
# Использованный метод: append()
# Текущее потребление памяти: 0.000522 мб
# Пик использования памяти: 3.994870 мб
# Операция заняла: 0.072619 секунд
# Функция make_list_with_append завершила работу
# ------------------------------------------------
# Название функции: make_list_concatenation
# Использованный метод: конкатенация
# Текущее потребление памяти: 0.000526 мб
# Пик использования памяти: 4.791808 мб
# Операция заняла: 21.387560 секунд
# Функция make_list_concatenation завершила работу
# ------------------------------------------------