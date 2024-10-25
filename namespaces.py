from package1.package2.package3.module3 import d # d = 7

def square(x):
    # global d
    d = x ** 3
    def even(x):
        nonlocal d
        d = x * 100
        return f'even = {d}'
    print(even(x)) # 7
    return f'square = {d}'

d = 3
print(f'global = {d}')
print(square(2)) # 7
print(f'global = {d}')
# global = 3
# even = 200
# square = 200
# global = 3