# пример 1 - блоки try и except
# try:
#     i = 0
#     print(10 / i)
#     print('Done')
# except:
#     print('Нельзя делить на ноль')


# пример 2 - нужно указывать конкретную ошибку
# try:
#     i = 0
#     print(10 / i)
#     print('Done')
# except ZeroDivisionError: # указываем имя класса
#     print('Нельзя делить на ноль')


# пример 3 - можно перечислять классы ошибок, если обработка их одинаковая
# try:
#     truba = a + b
#     truba1 = 10 / i
# except (ZeroDivisionError, NameError): # указываем имена классов
#     print('Что-то пошло не так, но мы устояли')


# пример 4 - можно на каждый класс ошибок писать свой обработчик
# try:
#     x = a + b
#     y = 10 / i
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# except NameError: # указываем имена классов
#     print('Нет такой переменной')
# Нет такой переменной

# пример 5-6 - можно сохранять класс ошибки в переменную
# try:
#     a = 10 / 0
# except ZeroDivisionError as exc:
#     print(f'Вот, что пошло не так: {exc}')
# Вот, что пошло не так: division by zero

# пример 7 - с ошибкой прилетают аргументы ошибки - name_var.args
# try:
#     file = open('xxx.txt', 'r')
# except OSError as exc:
#     print(f'Вот, что пошло не так: {exc}, параметры: {exc.args}')
# Вот, что пошло не так: [Errno 2] No such file or directory: 'xxx.txt',
# параметры: (2, 'No such file or directory')
# finally:
#     print('Вот такая вот фигня приключилась')

# практика
print('Какой хороший день')
i = int(input('Введите число: '))
try:
    result = 10 * (1 / i)
except ZeroDivisionError as exc:
    print(f'Нельзя делить на ноль! {exc}')
else:
    print('Ура, мы не делим на ноль!')
finally:
    print('Завершаем урок!')