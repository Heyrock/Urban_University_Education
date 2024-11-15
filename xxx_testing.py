import math


class Figure:
    sides_count = 0

    def __init__(self, rgb, *sides):
        self.__color = list(rgb) if self.__is_valid_color(*rgb) else [0, 0, 0]
        self.filled = False
        self.sides = sides

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(map(lambda x: x in range(0, 256), (r, g, b)))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    @staticmethod
    def __check_positive(new_sides):
        return all(map(lambda x: x > 0, *new_sides))

    def __is_valid_sides(self, new_sides):
        return self.sides_count == len(new_sides) \
            and self.__check_positive(new_sides)
        # return self.sides_count == len(new_sides)

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        else:
            if len(new_sides) == 1 and isinstance(self, (Cube, Circle)):
                self.__sides = [new_sides[0]] * self.sides_count
            else:
                self.__sides = [1] * self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.side = sides[0]
        self.__radius = self.side / 2 * math.pi
        # self.sides = sides

    def get_square(self):
        return 2 * math.pi * self.__radius ** 2


# class Triangle(Figure):
#     sides_count = 3
#
#     def __init__(self, rgb, *sides):
#         super().__init__(rgb, *sides)
#         self.side = sides
#         self.__a, self.__b, self.__c = self.side
#
#     @staticmethod
#     def get_half_perimeter(a, b, c):
#         return (a + b + c) / 2
#
#     def get_square(self):
#         hp = self.get_half_perimeter(
#             self.__a,
#             self.__b,
#             self.__c
#         )
#         s = hp * (hp - self.__a) * (hp - self.__b) * (hp - self.__c)
#         return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.side = sides[0]

    def get_volume(self):
        return self.side ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color()) # [55, 66, 77]
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color()) # [222, 35, 130]
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides()) # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# circle1.set_sides(15) # Изменится
circle1.sides = 15 # Изменится
# print(circle1.get_sides()) # [15]
print(circle1.sides) # [15]
#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1)) # 15
#
# # Проверка объёма (куба):
# print(cube1.get_volume()) # 216