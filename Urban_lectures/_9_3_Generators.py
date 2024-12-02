# пример 1 - ленивые вычисления генераторами

my_numbers = [3, 1, 4]

result = (x ** 100 for x in my_numbers)
print(result)
# <generator object <genexpr> at 0x000001F6138798A0>

for elem in result:
    print(elem)
# 515377520732011331036461129765621272702107522001
# 1
# 1606938044258990275541962092341162602522202993782792835301376


# пример 2 - Прочитать генераторную сборку можно только один раз

my_numbers = [3, 1, 4]

result = (x ** 100 for x in my_numbers)

for elem in result:
    print(elem)

print('One more time')

for elem in result:
    print(elem)
# ничего


# пример 3 - Генераторные сборки используются там, где требуются затратные операции
import time

start = time.time()
my_numbers = [3, 1, 4, 4, 5, 6, 9, 7]

result = [x ** 3000 for x in my_numbers]
print(result)

for elem in result:
    print(elem)

finish = time.time()
print(f'Время в миллисекундах: {round(((finish - start) * 1000), 3)}')
# Время в миллисекундах: 5.996

start = time.time()
result = (x ** 3000 for x in my_numbers)
print(result)

for elem in result:
    print(elem)

finish = time.time()
print(f'Время в миллисекундах: {round(((finish - start) * 1000), 3)}')
# Время в миллисекундах: 2.998


# пример 4 - Демонстрация встроенных функций с ленивыми вычислениями
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 0]

ran = range(10, 30)
zp = zip(list_1, list_2)
mp = map(str, list_1)

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))

# range(10, 30) <zip object at 0x000001EACF50EC80> <map object at 0x000001EACF38BA30>
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# [(1, 6), (2, 7), (3, 8), (4, 9), (5, 0)]
# ['1', '2', '3', '4', '5']

