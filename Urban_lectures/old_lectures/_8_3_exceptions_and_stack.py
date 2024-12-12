# Пример 1 - ошибка летит по стеку вызовов
def f1(number):
    print('Функция ф1')
    return 10 / number


def f2():
    print('Функция ф2')
    result_f1 = f1(0)
    return result_f1


try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'Что-то пошло не так - {exc}, но мы держимся.')

# Функция ф2
# Функция ф1
# Что-то пошло не так - division by zero, но мы держимся.

# Пример 2 - ошибка летит по стеку вызовов
def f1(number):
    print('Функция ф1')
    return 10 / number


def f2():
    print('Функция ф2')
    summ = 0
    for i in range (-2, 2):
        summ += f1(i)
    return summ


try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'Вот, что пошло не так - {exc}, но мы держимся.')

# Функция ф2
# Функция ф1
# Функция ф1
# Функция ф1
# Вот, что пошло не так - division by zero, но мы держимся.

# Пример 3 - перехват ошибки на уровне, где она была сформирована
def f1(number):
    print('Функция ф1')
    return 10 / number


def f2():
    print('Функция ф2')
    summ = 0
    for i in range (-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'Внутри f1 что-то пошло не так - {exc}, но работает.')
    return summ / 0


try:
    print(f2())
except ZeroDivisionError as exc:
    print(f'Внутри f2 что-то пошло не так - {exc}, но мы устояли.')
# Функция ф2
# Функция ф1
# -5.0
# Функция ф1
# -15.0
# Функция ф1
# Внутри f1 что-то пошло не так - division by zero, но работает.
# Функция ф1
# -5.0
# Внутри f2 что-то пошло не так - float division by zero, но мы устояли.