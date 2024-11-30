# пример 1 - почему функция - это объект

def get_russian_names():
    print(['Ваня', 'Коля', 'Маша'])


get_russian_names()

print(type(get_russian_names))
# ['Ваня', 'Коля', 'Маша']
# <class 'function'>


# пример 2 - функцию можно присвоить переменной

def get_russian_names():
    return(['Ваня', 'Коля', 'Маша'])


print(get_russian_names.__name__)
# get_russian_names
my_func = get_russian_names
print(my_func())
# ['Ваня', 'Коля', 'Маша']
print(my_func.__name__)
# get_russian_names


# пример 3 - С функцией можно работать, как с обычными объектами

def get_russian_names():
    return(['Ваня', 'Коля', 'Маша'])


def get_british_names():
    return(['Oliver', 'Jack', 'Harry'])


name_getters = [get_russian_names, get_british_names]

for name_getter in name_getters:
    print(name_getter())

# ['Ваня', 'Коля', 'Маша']
# ['Oliver', 'Jack', 'Harry']


# пример 4 - Функции, принимающие на вход другие функции с аргументами

def adder(arg):
    res = 0
    for number in arg:
        res += number
    return res


def multiplier(arg):
    res = 1
    for number in arg:
        res *= number
    return res


def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Получилось: {result}')


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

process_numbers(numbers=my_numbers, function=adder)
# Получилось: 31
process_numbers(numbers=my_numbers, function=multiplier)
# Получилось: 6480


# пример 5 - функция map

def mul_by_2(x):
    return x * 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = map(mul_by_2, my_numbers)
print(list(result))
# [6, 2, 8, 2, 10, 18, 4, 12]


# пример 6 - функция filter

def is_odd(x):
    return x % 2

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = filter(is_odd, my_numbers)
print(list(result))
# [3, 1, 1, 5, 9]



