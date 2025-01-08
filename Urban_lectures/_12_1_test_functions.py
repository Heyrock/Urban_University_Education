import _12_1_calculator as calc


def test_add():
    if calc.add(1, 2) == 3:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) FAILED')


def test_sub():
    if calc.sub(1, 2) == -1:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) FAILED')


def test_mul():
    if calc.mul(3, 2) == 6:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) FAILED')


def test_div():
    if calc.sub(4, 2) == 2:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) FAILED')


if __name__ == '__main__':
    test_add()
    test_sub()
    test_mul()
    test_div()