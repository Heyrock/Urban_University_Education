import operator

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
x = 3

print(operator.concat(a, b))
# [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print(operator.contains(a, x))
# True
print(operator.countOf(a, x))
# 1


# Если очередь ещё не пуста (метод empty) и один из столов освободился