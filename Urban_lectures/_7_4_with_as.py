import io
from pprint import pprint

name = 'sample2.txt'

# with open(name, encoding='utf8') as file:
#     for line in file:
#         print(line, end='')

with open(name, encoding='utf8') as file:
    for line in file:
        for char in line:
            print(char, end='')
    print()
    print(file.tell())
# Привет, я новый текст
# Вторая строка нового текста