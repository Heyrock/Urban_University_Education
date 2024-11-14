# Дополнительное практическое задание по модулю: "Наследование классов."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного
# уровня сложности
#
# Задание "Они все так похожи":
# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D
# подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
#
# Вы когда-нибудь задумывались как устроены графические библиотеки для языков
# программирования?
#
# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но...
# Что лежит в основе удобного использования таких объектов?
#
# По названию задачи можно понять, что все геометрические фигуры обладают схожими
# свойствами, такими как: длины сторон, цвет и др.
#
# Давайте попробуем реализовать простейшие классы для некоторых таких фигур и
# при этом применить наследование (в будущем, изучая сторонние библиотеки,
# вы будете замечать схожие классы, уже написанные кем-то ранее):
#
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
#
# Многие атрибуты и методы должны быть инкапсулированны и для них должны
# быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
#
# Подробное ТЗ:
#
# Атрибуты класса Figure: sides_count = 0
#
# Каждый объект класса Figure должен обладать следующими атрибутами:
#
# 1. Атрибуты(инкапсулированные):
# __sides(список сторон (целые числа)),
# __color(список цветов в формате RGB)
# 2. Атрибуты(публичные):
# filled(закрашенный, bool)
#
# И методами:
#
# 1. Метод get_color, возвращает список RGB цветов.
# 2. Метод __is_valid_color - служебный, принимает параметры r, g, b,
# который проверяет корректность переданных значений перед установкой
# нового цвета.
# Корректный цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255
# (включительно).
# 3. Метод set_color принимает параметры r, g, b - числа и изменяет атрибут
# __color на соответствующие значения, предварительно проверив их на корректность.
# Если введены некорректные данные, то цвет остаётся прежним.
# 4. Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
# возвращает True если все стороны целые положительные числа и кол-во новых сторон
# совпадает с текущим, False - во всех остальных случаях.
# 5. Метод get_sides должен возвращать значение атрибута __sides.
# 6. Метод __len__ должен возвращать периметр фигуры.
# 7. Метод set_sides(self, *new_sides) должен принимать новые стороны, если их
# количество не равно sides_count, то не изменять, в противном случае - менять.
#
#
# Атрибуты класса Circle: sides_count = 1
#
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
#
# 1. Все атрибуты и методы класса Figure
# 2. Атрибут __radius, рассчитать, исходя из длины окружности
# (одной единственной стороны).
# 3. Метод get_square возвращает площадь круга (можно рассчитать как через длину,
# так и через радиус).
#
#
# Атрибуты класса Triangle: sides_count = 3
#
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# 1. Все атрибуты и методы класса Figure
# 2. Метод get_square возвращает площадь треугольника.
# (можно рассчитать по формуле Герона)
#
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
#
# 1. Все атрибуты и методы класса Figure.
# 2. Переопределить __sides сделав список из 12 одинаковых сторон
# (передаётся 1 сторона)
# 3. Метод get_volume, возвращает объём куба.
#
#
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон,
# если сторон не равно sides_count, то создать массив с единичными сторонами и
# в том кол-ве, которое требует фигура.
#
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1,
# то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3,
# то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его
# стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12,
# то его стороны будут - [1, 1, 1, ....., 1]
#
#
# Код для проверки:
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
#
# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
#
#
# Примечания (рекомендации):
#
# 1. Рекомендуется сделать дополнительные (свои проверки) работы методов
# объектов каждого класса.
# 2. Делайте каждый класс и метод последовательно и проверяйте работу
# каждой части отдельно.
# 3. Для проверки принадлежности к типу рекомендуется использовать функцию
# isinstance.
# 4. Помните, служебные инкапсулированные методы можно и нужно использовать
# только внутри текущего класса.
# 5. Вам не запрещается вводить дополнительные атрибуты и методы, творите,
# но не переборщите!

import math


class Figure:
    sides_count = 0

    def __init__(self, rgb, *sides):
        # это так специально, чтобы соблюсти некорректное условие задания :)
        if len(sides) == 1 and isinstance(self, (Cube, Circle)):
            self.__sides = [sides[0]] * self.sides_count
        elif len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

        self.__color = list(rgb) if self.__is_valid_color(*rgb) else [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(map(lambda x: x in range(0, 256), (r, g, b)))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    @staticmethod
    def __check_positive(*new_sides):
        return all(map(lambda x: x > 0, *new_sides))

    def __is_valid_sides(self, *new_sides):
        return len(self.__sides) == len(new_sides) \
            and self.__check_positive(*new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.side = sides[0]
        self.__radius = self.side / 2 * math.pi

    def get_square(self):
        return 2 * math.pi * self.__radius ** 2

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.side = sides
        self.a, self.b, self.c = self.side
        # if len(sides) == self.sides_count:
        #     self.a = sides[0]
        #     self.b = sides[1]
        #     self.c = sides[2]

    @staticmethod
    def get_half_perimeter(a, b, c):
        return (a + b + c) / 2

    def get_square(self):
        hp = self.get_half_perimeter(
            self.a,
            self.b,
            self.c
        )
        s = hp * (hp - self.a) * (hp - self.b) * (hp - self.c)
        return s

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        if len(side) == self.sides_count:
            self.__side = side
        else:
            self.__side = [1, 1, 1]


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.side = sides[0]

    def get_volume(self):
        return self.side ** 3

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color()) # [55, 66, 77]
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color()) # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides()) # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15) # Изменится
print(circle1.get_sides()) # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1)) # 15

# Проверка объёма (куба):
print(cube1.get_volume()) # 216

t = Triangle((1, 2, 3), 4, 5, 6)
print(t.__dict__)
print(t.side)
print(t.get_square())