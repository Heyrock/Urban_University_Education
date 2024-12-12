# синтаксис генератора

def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1


# пример 1 - создание простого генератора

def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1

obj = func_generator(10)
print(obj)
# <generator object func_generator at 0x00000244BC239150>
print(list(obj))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in obj:
    print(i, end=' ')
# 0 1 2 3 4 5 6 7 8 9


# пример 2 - функция Фибоначчи

def fib_standard(n):
    lst = []
    a, b = 0, 1
    for _ in range(n):
        lst.append(a)
        a, b = b, a + b
    return lst


def fib_gen(n):
    i = 0
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(fib_standard(10))
print(list(fib_gen(10)))


# пример 3 - можно сделать бесконечный "список" значений
def fib_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for i in fib_v3():
    print(i)
    if i > 10 ** 6:
        break


# пример 4 - быстродействие генератора
import time

start = time.time()

def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            yield line.strip()


for line in read_large_file('xxx_ToDo_1.txt'):
    print(line)

fin = time.time()
print(f'время срабатывания {round(((fin - start) * 1000), 3)}')
# время срабатывания 0.999
