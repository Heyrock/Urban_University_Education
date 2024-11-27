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