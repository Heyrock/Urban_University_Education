# Домашнее задание по уроку "Пространство имен"
#
# 1. Создайте новый проект в PyCharm
# 2. Запустите созданный проект
# Ваша задача:
#
# 1. Создайте новую функцию test_function
# 2. Создайте внутри test_function другую функцию - inner_function,
# Эта функция должна печатать значение "Я в области видимости функции test_function"
# 3. Вызовите функцию inner_function внутри функции test_function
# 4. Попробуйте вызывать inner_function вне функции test_function
# и посмотрите на результат выполнения программы.
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function()
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
