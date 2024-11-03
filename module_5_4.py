# Задача "История строительства":
#
# Для решения этой задачи будем пользоваться решением к предыдущей задаче
# "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить
# названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта,
# тем более можно удобно обращаться к атрибутам класса используя ссылку
# на сам класс - cls.
#
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
#
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов
# __del__ и __new__, а также значение атрибута houses_history.
def check_instance(f):
    def wrapper(*args):
        if isinstance(args[1], House):
            return f(*args)
        else:
            return 'Вы сравниваете несравниваемое'
    return wrapper


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number}'

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(repr('Такого этажа не существует'))

    def __len__(self):
        return self.number

    @check_instance
    def __eq__(self, other):
        return self.number == other.number

    @check_instance
    def __lt__(self, other):
        return self.number < other.number

    @check_instance
    def __le__(self, other):
        return self.number <= other.number

    @check_instance
    def __gt__(self, other):
        return self.number > other.number

    @check_instance
    def __ge__(self, other):
        return self.number >= other.number

    @check_instance
    def __ne__(self, other):
        return self.number != other.number

    def __add__(self, value):
        if isinstance(value, House):
            self.number += value.number
        elif isinstance(value, int):
            self.number += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)
    # Прочие арифметические действия удалил, чтобы не мешали

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
