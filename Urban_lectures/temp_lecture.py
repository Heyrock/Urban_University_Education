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