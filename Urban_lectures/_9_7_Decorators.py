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