# пример 6 - функция filter

def is_odd(x):
    return x % 2

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = filter(is_odd, my_numbers)
print(list(result))
# [3, 1, 1, 5, 9]