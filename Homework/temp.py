# пример 6 - создание на лету множеств и словарей

nums_1 = [3, 1, 4, 1, 5, 9, 2, 6]
nums_2 = [10, 20, 30]
print({x for x in nums_1})
# {1, 2, 3, 4, 5, 6, 9}

print({x: x * 2 for x in nums_1})
# {3: 6, 1: 2, 4: 8, 5: 10, 9: 18, 2: 4, 6: 12}

nums_1.extend(nums_2)
print(nums_1)