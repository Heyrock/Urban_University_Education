# def my_sum(n, *args, txt='Сумма чисел:'):
#     s = 0
#     for i in range(len(args)):
#         s += args[i] ** n
#         print(i ** n)
#     print(txt, s)
#
# my_sum(3, 1, 2, 3, 4, 5)

def my_sum(n, *args, txt='Сумма чисел:'):
    s = 0
    for i in args:
        s += i ** n
        print(i ** n)
    print(txt, s)

my_sum(3, 1, 2, 3, 4, 5, txt='rrrr')