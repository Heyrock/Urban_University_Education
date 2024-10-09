def test(x, y):
    if check(x, y):
        print('Ok')
    elif check_2(x, y):
        print('X is larger')
    elif check_3(x, y):
        print('Y is larger')
    else:
        print('Whatever')

def check(x, y):
    return x == y


def check_2(x, y):
    return x > y

def check_3(x, y):
    return x < y

test(0, 0)