# __slots__ & property

class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.__length = (x ** 2 + y ** 2) ** 0.5
        self.__length = 0

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


pt2 = Point2D(1, 2)
print(pt2.length)
# 2.23606797749979
pt2.length = 10
print(pt2.length)
# 10

# __slots__ & наследование