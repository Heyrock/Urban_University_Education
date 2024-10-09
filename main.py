# Задание 4
# Напишите программу, которая получает от пользователя строку текста
# и число n, а затем выводит вложенный список, в котором n последовательных
# элементов принадлежат разным подспискам.
string = 'абвгдеёжз'
num = 3
matrix = []
count = 0

for i in range(num):
    matrix.append([])
    for j in range(count, len(string), num):
        matrix[i].append(string[j])
    count += 1

[print(*matrix[i]) for i in range(len(matrix))]

# ИЛИ:

string = list(input())
num = int(input())
matrix = []

for i in range(num):
    matrix.append(string[i::num])
print(matrix)