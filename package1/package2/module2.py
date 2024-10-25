def add(x):
    return x + 10


def multiply(x):
    return x * 5


def super_function(function1, function2):
    return lambda x: function1(function2(x))


print(super_function(add, float)('16'))
print(super_function(tuple, multiply)((3, 4, 5)))
print(super_function(str, multiply)('55'))
print(super_function(list, multiply)((1, 2, 3)))
# 26.0
# (3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5)
# 5555555555
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]