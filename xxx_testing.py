import math


class Figure:
    sides_count = 3

    def __init__(self, rgb, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1 for i in range(self.sides_count)]
        else:
            self.__sides = [i for i in sides]

        self.__color = [i for i in rgb]
        self.filled = False  # ???

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
            self.__sides = [new_sides]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return  # переопределить у дочерей


# class Circle(Figure):
#     sides_count = 1
#
#     def __init__(self, rgb, *sides):
#         super().__init__(rgb)
#         self.side = sides[0]
#         self.__radius = self.side / 2 * math.pi
#
#     def get_square(self):
#         return 2 * math.pi * self.__radius ** 2
#
#
# class Triangle(Figure):
#     sides_count = 3
#
#     def __init__(self, rgb, *sides):
#         super().__init__(rgb, *sides)
#         # self.__sides = [i for i in sides]
#         # self.a = sides[0]
#         # self.b = sides[1]
#         # self.c = sides[2]
#
#     @staticmethod
#     def get_half_perimeter(a, b, c):
#         return (a + b + c) / 2
#
#     def get_square(self):
#         hp = self.get_half_perimeter(
#             self.a,
#             self.b,
#             self.c
#         )
#         s = hp * (hp - self.a) * (hp - self.b) * (hp - self.c)
#         return s
#
#
# class Cube(Figure):
#     sides_count = 12
#
#     def __init__(self, rgb, side):
#         super().__init__(rgb)
#         self.side = side
#
#     def get_volume(self):
#         return self.side ** 3


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

# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
f = Figure((1, 2, 3), 0)
print(f.__dict__)