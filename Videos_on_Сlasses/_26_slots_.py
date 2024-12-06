import timeit

class Point:
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y', 'z')
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt = Point(1, 2)
pt2 = Point2D(10, 20)

t1 = timeit.timeit(pt.calc)
t2 = timeit.timeit(pt2.calc)
print(t1, t2)
# 0.2045 0.1876


# print(pt.MAX_COORD)
# # 100
#
# print(pt.__sizeof__() + pt.__dict__.__sizeof__())
# # 304
# print(pt.__sizeof__())
# # 40