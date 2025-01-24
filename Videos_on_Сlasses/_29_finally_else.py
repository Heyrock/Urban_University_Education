try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as exc:
    print(exc)
except ValueError as exc:
    print(exc)
# invalid literal for int() with base 10: 'a'

print('Штатное завершение работы')

# -----------

try:
    x, y = map(int, input().split()) # 1 2
    res = x / y
except ZeroDivisionError as exc:
    print(exc)
except ValueError as exc:
    print(exc)
else:
    print('Не произошло никаких исключений')
# Не произошло никаких исключений
finally:
    print('Блок finally выполняется всегда')
# Блок finally выполняется всегда

# ------------

try:
    f = open('__init__.py')
    f.write('sth')
except FileNotFoundError as z:
    print(z)
except:
    print('Нельзя записывать в файл, открытый для чтения')
finally:
    if f:
        f.close()
        print('Файл закрыт')
# Нельзя записывать в файл, открытый для чтения
# Файл закрыт

# ------------

def get_values():
    try:
        x, y = map(int, input().split()) # f b
        return x, y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print('finally выполняется до return')

print(get_values())
# invalid literal for int() with base 10: 'f'
# finally выполняется до return
# (0, 0)

# ------------

try:
    x, y = map(int, input().split()) # 1 0
    try:
        res = x / y
    except ZeroDivisionError:
        print('Деление на ноль')
except ValueError as z:
    print(z)
# Деление на ноль

# -----------

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Деление на ноль'

try:
    x, y = map(int, input().split()) # 1 0
    print(div(x, y))
except ValueError as z:
    print(z)
# Деление на ноль