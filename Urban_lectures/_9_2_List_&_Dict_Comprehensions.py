# пример 4 - условия перед циклом
# (не фильтрует данные, а меняет операцию с ними)

my_numbers = ['A', 1, 4, 'B', 5, 'C', 2, 6]
result = [x if type(x) == str else x * 5 for x in my_numbers]
print(result)


# пример 5 - вложенные циклы

nums_1 = [3, 1, 4, 1, 5, 9, 2, 6]
nums_2 = [2, 7, 1, 8, 2, 8, 1, 8]

print([x * y for x in nums_1 for y in nums_2])
print([x * y for x in nums_1 for y in nums_2 if x % 2])
print([x * y for x in nums_1 for y in nums_2 if x % 2 and y // 2])


# пример 6 - создание на лету множеств и словарей

nums_1 = [3, 1, 4, 1, 5, 9, 2, 6]
print({x for x in nums_1})
# {1, 2, 3, 4, 5, 6, 9}

print({x: x * 2 for x in nums_1})
# {3: 6, 1: 2, 4: 8, 5: 10, 9: 18, 2: 4, 6: 12}
