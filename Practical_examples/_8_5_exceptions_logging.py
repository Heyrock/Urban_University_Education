def calc(line: str):
    num_1, operation, num_2 = line.split()
    num_1 = int(num_1)
    num_2 = int(num_2)
    if operation == '+':
        print(f'Результат: {num_1 + num_2}')
    if operation == '-':
        print(f'Результат: {num_1 - num_2}')
    if operation == '/':
        print(f'Результат: {num_1 / num_2}')
    if operation == '*':
        print(f'Результат: {num_1 * num_2}')
    if operation == '//':
        print(f'Результат: {num_1 // num_2}')
    if operation == '%':
        print(f'Результат: {num_1 % num_2}')


counter = 0

with open('data.txt', 'r') as file:
    for line in file:
        counter += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в строке {counter}: '
                      'не хватает данных в строке')
            else:
                print(f'Ошибка в строке {counter}: '
                      'нельзя перевести в число')
