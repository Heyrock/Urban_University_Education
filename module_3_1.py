# Задача "Счётчик вызовов":
#
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
#
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
#
# 1. Функция count_calls подсчитывающая вызовы остальных функций.
#
# 2. Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
#
# 3. Функция is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#
# Пункты задачи:
#
# 1. Создать переменную calls = 0 вне функций.
#
# 2. Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях.
#
# 3. Создать функцию string_info с параметром string и реализовать логику работы по
# описанию.
#
# 4. Создать функцию is_contains с двумя параметрами string и list_to_search,
# реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз
# с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).
#
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)
#
# Вывод на консоль:
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4
#
# Примечания:
#
# 1. Для использования глобальной переменной внутри функции используйте
# оператор global.
# 2. Для функции is_contains лучше привести и искомую строку и все строки в
# списке в один регистр.
def count_calls():
    global calls
    calls += 1


def string_info(string: str) -> tuple:
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(
        string: str,
        list_to_search: list
) -> bool:
    count_calls()
    string = string.lower()
    list_to_search = [
        i.lower() if i.isalpha() else i for i in list_to_search
    ]
    # return True if string in list_to_search else False
    return string in list_to_search


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
