# Пример 1 - библиотека itertools
import sys
from itertools import repeat

ex_iterator = repeat('4', 100_000)
print(ex_iterator)
print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')
# repeat('4', 100000)
# Размер итератора - 48

ex_str = '4' * 100_000
print(f'Размер списка - {sys.getsizeof(ex_str)}')
# Размер списка - 100049


# пример 2 - создание итератора
class Iter:
    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 0
        # возвращаем ссылку на себя, т.к. сам объект должен быть итератором
        return self

    def __next__(self):
        # этот метод возвращает значения по требованию питона (ленивые вычисления)
        self.i += 1
        if self.i == 1:
            return self.first
        elif self.i == 2:
            return self.second
        elif self.i == 3:
            return self.third
        elif self.i == 4:
            return 'Подсчет закончен'
        raise StopIteration  # признак того, что возвращать больше нечего


obj = Iter()
print(obj)
# <__main__.Iter object at 0x0000023029574350>

for value in obj:
    print(value)
# Первый элемент
# Второй элемент
# Третий элемент
# Подсчет закончен


# т.е. интерпретатор вызывает __next__ при каждом прохождении цикла
# если в __next__ возникает исключение StopIteration, это значит, что в объекте больше нет элементов, цикл прекращается.


# пример 3 - принцип действия цикла for по итератору
class Iter:
    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 0
        # возвращаем ссылку на себя, т.к. сам объект должен быть итератором
        return self

    def __next__(self):
        # этот метод возвращает значения по требованию питона (ленивые вычисления)
        self.i += 1
        if self.i == 1:
            return self.first
        elif self.i == 2:
            return self.second
        elif self.i == 3:
            return self.third
        elif self.i == 4:
            return 'Подсчет закончен'
        raise StopIteration  # признак того, что возвращать больше нечего


obj = Iter()

try:
    while True:
        print(obj.__next__())
except StopIteration:
    pass
# Первый элемент
# Второй элемент
# Третий элемент
# Подсчет закончен


# т.е. интерпретатор вызывает __next__ при каждом прохождении цикла
# если в __next__ возникает исключение StopIteration, это значит, что в объекте больше нет элементов, цикл прекращается.


# пример 4 - числа Фибоначчи - список vs. генератор
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n + 1):
        result.append(a)
        a, b = b, a + b
    return result


for value in fibonacci(n=10):
    print(value, end=' ')
# 0 1 1 2 3 5 8 13 21 34 55
print()


class Iter:
    def __init__(self, n):
        self.n = n + 1
        self.a = 0
        self.b = 1
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.n:
                raise StopIteration
            self.a, self.b = self.b, self.a + self.b
        return self.a


obj = Iter(10)

for i in obj:
    print(i, end=' ')
# 0 1 1 2 3 5 8 13 21 34 55