def my_func(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * my_func(int(str_number[1:]))


result = my_func(12345)
print(result)
