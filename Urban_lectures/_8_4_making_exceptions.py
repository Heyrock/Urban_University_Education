#  Пример 1 - raise ошибки

def greet_person(person_name):
    if person_name == 'ВоланДеМорт':
        raise Exception(f'Мы не любим тебя, {person_name}')
    print(f'Привет, {person_name}')


greet_person('Дорогой ученик')
greet_person('ВоланДеМорт')


#  Пример 2 - raise ошибки, но перед этим мы ее обрабатываем

try:
    # x = 10 / 0
    raise NameError('Hello there')
# except ZeroDivisionError as exc:
#     print('На ноль делить нельзя')
except NameError as exc:
    print(f'исключение типа {type(exc)} пролетело мимо! Его параметры {exc.args}')
    raise #


#  Пример 3 - создание класса-исключения

class ProZero(Exception):
    pass


def f(a, b):
    if b == 0:
        raise ProZero('Деление на ноль невозможно')
    return a / b


print(f(10, 0))
# ProZero: Деление на ноль невозможно


#  Пример 4 - создание класса-исключения и перехват ошибки
class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a, b):
    if b == 0:
        raise ProZero(
            message='Деление на ноль невозможно',
            extra_info={'a': a, 'b': b}
        )
    return a / b

try:
    print(f(10, 0))
except ProZero as exc:
    print('Не очень хороший день, мы словили ошибку')
    print(f'Сообщение об ошибке: "{exc.message}"')
    print(f'Дополнительная информация: {exc.extra_info}')

# Не очень хороший день, мы словили ошибку
# Сообщение об ошибке: "Деление на ноль невозможно"
# Дополнительная информация: {'a': 10, 'b': 0}
