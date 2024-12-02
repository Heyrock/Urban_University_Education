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