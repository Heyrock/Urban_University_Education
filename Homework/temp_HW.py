def my_func():
    return 10

res = sum([my_func() for i in range(3)])
print(res)