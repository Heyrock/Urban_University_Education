# Задание "Программистам всё можно":
# Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы
# не можем сложить число(int) и строку(str)? Давайте исправим это недоразумение!
#
# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)
#
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами
# (int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой),
# то возвращать строковое представление этих двух данных вместе (в том же порядке).
# Во всех остальных случаях выполнять стандартные действия.
#
# Пример кода:
# print(add_everything_up(123.456, 'строка'))
# print(add_everything_up('яблоко', 4215))
# print(add_everything_up(123.456, 7))
#
# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456
def add_everything_up(a, b):
    try:
        result = a + b
        if isinstance(result, float):
            return round(result, 3)
        return result
    except TypeError:
        return str(a) + str(b)


# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456

# ВАРИАНТ ЧЕРЕЗ КЛАСС И DECIMAL

# from decimal import Decimal
#
#
# class add_everything_up:
#     def __init__(self, a, b):
#         self.a = self.make_decimal(a)
#         self.b = self.make_decimal(b)
#
#     @staticmethod
#     def make_decimal(x):
#         if isinstance(x, (int, float)):
#             return Decimal(str(x))
#         else:
#             return x
#
#     def add(self):
#         try:
#             return self.a + self.b
#         except TypeError:
#             return str(self.a) + str(self.b)
#
#     def __str__(self):
#         return str(self.add())


# Пример кода:
# print(add_everything_up(123.456, 'строка'))
# print(add_everything_up('яблоко', 4215))
# print(add_everything_up(123.456, 7))

# 123.456строка
# яблоко4215
# 130.456