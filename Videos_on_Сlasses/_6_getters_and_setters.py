from accessify import private, protected

class Point:
    # @private
    # @classmethod
    # def check_value(cls, arg):
    #     return type(arg) in (int, float)

    @classmethod
    def __check_value(cls, arg):
        return type(arg) in (int, float)

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(*pt.get_coord()) # 10 20
# print(dir(pt))
# ['_Point__check_value', '_Point__x', '_Point__y', ...]
# print(dir(Point))
# print(pt._Point__x) # 10
print(pt.__check_value(5))
# Point.check_value() is inaccessible due to its protection level