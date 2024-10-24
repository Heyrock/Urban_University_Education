import math


def square(x):
    global a, print
    def print(*args):
        return 'Ok'
    print(1, globals(), 1)
    # 'square': <function square at 0x000001965D790540>, 'a': 5}
    a = x ** 2
    print(2, globals(), 2)
    # 'a': 4, 'square': <function square at 0x0000026380300540>}
    print(3, locals(), 3)
    # {'x': 2, 'a': 4}
    return a


a = 5
print(4, a, 4)
# 5
b = square(2)
print(5, b, 5)
# 4
print(6, a, 6) # После вызова функции
# 4
print(7, globals(), 7)
# 'square': <function square at 0x0000026380300540>, 'a': 5, 'b': 4}

# 'square': <function square at 0x000001965D790540>, 'a': 5}