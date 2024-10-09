def func_with_params(a, b=None):
    if b is None:
        b = []
        b.append(a)
    print(b)


[func_with_params(3) for i in range(3)]

# [3]
# [3, 3]
# [3, 3, 3]