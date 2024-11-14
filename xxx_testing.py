# 1) У фигуры количество сторон должно быть 0.
# 2) У круга, треугольника и куба sides также должны быть инкапсулированы. 
# Хорошие новости - Вы можете получить к ним доступ через get_sides.
# 
# Вот и все, в остальном все замечательно реализовано.
# 
# Рекомендация:
# 
# Метод init в том же родительском классе можно сделать чуть более гибким 
# (Ваш вариант тоже рабочий):
def __init__(self, rgb, *sides):
    self.__color = list(rgb) if self.__is_valid_color(*rgb) else [0, 0, 0]
    if len(sides) == self.sides_count and self.__is_valid_sides(*sides):
        self.__sides = list(sides)
    else:
        self.__sides = [1] * self.sides_count
    self.filled = False