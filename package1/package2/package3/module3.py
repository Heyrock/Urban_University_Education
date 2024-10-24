# Задание 6
# В предыдущих статьях мы неоднократно использовали встроенную функцию zip()
# для параллельной итерации двух наборов данных.

# Напишите функцию высшего порядка, которая возвращает функции для:
#
# 1. Группировки параллельных элементов списков с помощью самописной my_zip().
# 2. Конкатенации элементов, сгрупированных my_zip().
# 3. Сложения элементов, сгруппированных my_zip().

# Примечание: следует учесть, что получаемые от пользователя списки могут
# быть разной длины.
# Как и встроенная zip(), my_zip() должна ограничивать размер возвращаемого
# списка длиной более короткого набора данных.

# (5, 4) (8, 5) (9, 6) (8, 2) (3, 3) (12, 2) (3, 5) (5, 9) (5, 4) (4, 12) (0, 9) (9, 3)
# 54 85 96 82 33 122 35 59 54 412 09 93
# 9 13 15 10 6 14 8 14 9 16 9 12
def convert(*args):
    return (list(map(int, arg.split())) for arg in args)


def zipp(*args):
    lst_1, lst_2 = args
    length = min(len(lst_1), len(lst_2))
    new_list = []
    for i in range(length):
        new_list.append((lst_1[i], lst_2[i]))
    return new_list


def concatenate(*args):
    lst_1, lst_2 = args
    length = min(len(lst_1), len(lst_2))
    new_list = []
    for i in range(length):
        new_list.append(str(lst_1[0]) + str(lst_1[1]))
    return new_list


def my_zip(f):
    def medium(*args):
        return f(*args)
    return medium


input_1 = '5 8 9 8 3 12 3 5 5 4 0 9 6 1 23 6 12 30'
input_2 = '4 5 6 2 3 2 5 9 4 12 9 3'
joint = convert(input_1, input_2)
joint2 = convert(input_1, input_2)


print(my_zip(zipp)(*joint))
print(my_zip(zipp)(*joint))
print(my_zip(concatenate)(*joint2))


# print(zipp(list_1, list_2))