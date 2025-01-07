import random

# m = random.randint(1, n := int(input('Введите число: ')))

n = int(input('Введите число: '))
m = random.randint(1, n)
print(f'm = {m}, результат = {m % n + 1}')

# Введите число: 10
# m = 5, результат = 6

