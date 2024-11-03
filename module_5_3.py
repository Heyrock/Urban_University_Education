# Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.
#
# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче
# "Специальные методы класса".
#
# Необходимо дополнить класс House следующими специальными методами:
#
# __eq__(self, other) - должен возвращать True, если количество этажей
# одинаковое у self и у other.
#
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны
# присутствовать в классе и возвращать результаты сравнения по соответствующим
# операторам.
#
# Как и в методе __eq__ в сравнении участвует кол-во этажей.
#
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value,
# возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__
# (возвращают результат его вызова).
#
# Остальные методы арифметических операторов, где self - x, other - y:
#
# Следует заметить, что other может быть не только числом, но и вообще любым
# объектом другого класса.
#
# Для более точной логики работы методов __eq__, __add__  и других методов
# сравнения и арифметики перед выполняемыми действиями лучше убедиться в
# принадлежности к типу при помощи функции isinstance:
#
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.
#
# Пример результата выполнения программы:
def check_instance(f):
    def wrapper(*args):
        if isinstance(args[1], House):
            return f(*args)
        else:
            return 'Вы сравниваете несравниваемое'
    return wrapper

class House:
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

    # def __eq__(self, other):
    #     if isinstance(other, House):
    #         return self.number_of_floors == other.number_of_floors
    #     else:
    #         return 'Вы сравниваете несравниваемое'
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

    def __sub__(self, value):
        if isinstance(value, House):
            self.number -= value.number
        elif isinstance(value, int):
            self.number -= value
        return self

    def __isub__(self, value):
        return self.__sub__(value)

    def __rsub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        if isinstance(value, House):
            self.number *= value.number
        elif isinstance(value, int):
            self.number *= value
        return self

    def __imul__(self, value):
        return self.__mul__(value)

    def __rmul__(self, value):
        return self.__mul__(value)

    def __truediv__(self, value):
        if isinstance(value, House):
            if value.number == 0:
                raise ZeroDivisionError
            self.number /= value.number
        elif isinstance(value, int):
            if value == 0:
                raise ZeroDivisionError
            self.number /= value
        return self

    def __itruediv__(self, value):
        return self.__truediv__(value)

    def __rtruediv__(self, value):
        return self.__truediv__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# False
# Название: ЖК Эльбрус, кол-во этажей: 20
# True
# Название: ЖК Эльбрус, кол-во этажей: 30
# Название: ЖК Акация, кол-во этажей: 30
# False
# True
# False
# True
# False
