# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею
# другую функцию.
#
# Задание:
#
# Напишите 2 функции:
#
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат
# 1ой функции будет простым числом и "Составное" в противном случае.
#
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
#
# 1. Не забудьте написать внутреннюю функцию wrapper в is_prime
# 2. Функция is_prime должна возвращать wrapper
# 3. @is_prime - декоратор для функции sum_three
def is_prime(func):
    def wrapper(*args, **kwargs):
        summa = func(*args, **kwargs)
        digit = 'Простое'
        for i in range(2, summa // 2 + 1):
            if summa % i == 0:
                digit = 'Составное'
                break
        print(digit)
        return summa
    return wrapper


@is_prime
def sum_three(*args):
    summa = sum(args)
    return summa


result = sum_three(2, 3, 6)
print(result)
