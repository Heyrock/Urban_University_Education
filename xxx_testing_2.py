from dis import dis


def some_func():
    c = 'Я из третьего модуля'
    print('Я из третьего модуля')
    return c


print(some_func())
dis(some_func())


