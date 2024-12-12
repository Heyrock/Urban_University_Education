# Пример создания простого декоратора

def null_decorator(func):
    return func


def greet():
    return 'Hello!'

greet = null_decorator(greet)
greet1 = null_decorator(greet)

print(greet())
print(greet1())


# Пример 2 - синтаксис @
def null_decorator(func):
    return func

@null_decorator
def greet():
    return 'Hello!'


print(greet())


# Пример 3 - Добавляем функционал декоратору
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

greet_dec = uppercase(greet)

print(greet())
# HELLO!
print(greet_dec())
# HELLO!


# Пример 4 - пример декоратора
import time


def time_track(func):
    def surrogate(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end = time.time()
        elapsed = round(end - start, 4)
        print(f'Функция проработала: {elapsed} сек.')
        return result

    return surrogate


@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 50
    return len(str(total))


# result = digits(3141, 5926, 2718, 2818)
# print(result)
# Функция проработала: 0.0 сек.
# 708

surrogate = time_track(digits)
print(surrogate(3141, 5926, 2718, 2818))
# Функция проработала: 0.0 сек.
# 708


# Пример декоратора - счетчика времени

import time


def time_track(func):
    def surrogate(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end = time.time()
        elapsed = round(end - start, 4)
        print(f'Функция проработала: {elapsed} сек.')
        return result

    return surrogate


@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 50
    return len(str(total))

surrogate = time_track(digits)

result = digits(3141, 5926, 2718, 2818)
print(result)
# Функция проработала: 0.0 сек.
# 708

print(surrogate(3141, 5926, 2718, 2818))
# Функция проработала: 0.0 сек.
# 708

----------------------------------------
# пример 5 - Функция, генерирующая декораторы, которые генерируют функции-заместители
import sys
import time


def func_gen_dec(precision):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, *kwargs)
            end = time.time()
            elapsed = round(end - start, precision)
            print(f'Функция проработала: {elapsed} сек.')
            return res
        return wrapper
    return decorator


@func_gen_dec(precision=2)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10**5)


result = digits(3141, 5926, 2718, 2818)
print(result)

# # Либо, расшифровка без @
# time_track_prec_2 = func_gen_dec(precision=10)
# digits = time_track_prec_2(digits)
# result = digits(3141, 5926, 2718, 2818)
# print(result)

# # Либо, короче
# result = func_gen_dec(precision=2)(digits)(3141, 5926, 2718, 2818)
# print(result)
#
# # Функция проработала: 0.113779068 сек.
# # 70771

----------------------------------------
# пример 6 - расшифровка работы всех функций поэтапно
import sys
import time


def func_gen_dec(precision):
    print('Получили точность, с которой надо выводить результат')
    print('Начинаем создавать декоратор')
    def decorator(func):
        print(f'Декоратор принял на вход функцию, которую надо отдекорировать "{func.__name__}"')
        print('Начинает создавать функцию-обертку')
        def wrapper(*args, **kwargs):
            print(f'Мы в функции-обертке, которая заместит реальную функцию "{func.__name__}"')
            print('Засекаем время')
            start = time.time()
            print('Запускаем реальную функцию с переданными в нее параметрами и запоминаем результат')
            res = func(*args, *kwargs)
            print('Определяем затраченное время и выводим его')
            end = time.time()
            print('Применяем параметр precision, который получаем через замыкание')
            elapsed = round(end - start, precision)
            print(f'Функция проработала: {elapsed} сек.')
            print('Возвращаем результат, который вернула реальная функция')
            return res
        print('Декоратор создал функцию обертку и вернул ее')
        return wrapper
    print('Создан сам декоратор, возвращаем его')
    return decorator


@func_gen_dec(precision=2)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10**5)


result = digits(3141, 5926, 2718, 2818)
print(result)

# Получили точность, с которой надо выводить результат
# Начинаем создавать декоратор
# Создан сам декоратор, возвращаем его
# Декоратор принял на вход функцию, которую надо отдекорировать "digits"
# Начинает создавать функцию-обертку
# Декоратор создал функцию обертку и вернул ее
# Мы в функции-обертке, которая заместит реальную функцию "digits"
# Засекаем время
# Запускаем реальную функцию с переданными в нее параметрами и запоминаем результат
# Определяем затраченное время и выводим его
# Применяем параметр precision, который получаем через замыкание
# Функция проработала: 0.11 сек.
# Возвращаем результат, который вернула реальная функция
# 70771
