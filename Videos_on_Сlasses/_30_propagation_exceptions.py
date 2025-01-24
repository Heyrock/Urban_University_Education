def func2():
    return 1 / 0

def func1():
    return func2()

func1()

# Traceback (most recent call last):
#   File "C:\Users\...", line 7, in <module>
#     func1()
#   File "C:\Users\...", line 5, in func1
#     return func2()
#            ^^^^^^^
#   File "C:\Users\...", line 2, in func2
#     return 1 / 0
#            ~~^~~
# ZeroDivisionError: division by zero

# ---------------------

def func2():
    try:
        return 1 / 0
    except:
        print('Func2 error')


def func1():
    try:
        return func2()
    except:
        print('Func1 error')


try:
    func1()
except:
    print('Final call error')

# Func2 error

# --------------------