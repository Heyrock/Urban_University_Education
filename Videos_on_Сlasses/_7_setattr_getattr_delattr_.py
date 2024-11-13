class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        # if Point.MAX_COORD <= x <= Point.MIN_COORD:
        if self.MAX_COORD <= x <= self.MIN_COORD:
            self.x = x
            self.y = y

    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left

    # def __getattribute__(self, item):
    #     print('__getattribute__')
    #     return object.__getattribute__(self, item)

    # def __getattribute__(self, item):
    #     if item == 'z':
    #         raise ValueError('Доступ запрещен')
    #     else:
    #         # return object.__getattribute__(self, item)
    #         return super().__getattribute__(item)

    # def __setattr__(self, key, value):
    #     print('__setattr__')
    #     # object.__setattr__(self, key, value)
    #     super().__setattr__(key, value)

    # def __setattr__(self, key, value):
    #     if key == 'z':
    #         raise AttributeError('Недопустимое имя атрибута')
    #     elif value > 10:
    #         raise ValueError('Недопустимое значение атрибута')
    #     else:
    #         # object.__setattr__(self, key, value)
    #         super().__setattr__(key, value)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        # super().__setattr__('y', 5)

    def __getattr__(self, item):
        print('__getattr__:', item)
        return 'Такого атрибута не существует'

    def __delattr__(self, item):
        # object.__delattr__(self, item)
        super().__delattr__(item)


pt1 = Point(x=1, y=2)
# AttributeError: Недопустимое имя атрибута
# pt2 = Point(10, 20)
# pt1.z = 4
# print(pt1.yy)
del pt1.x
# __delattr__: x
print(pt1.__dict__)
# {'x': 1, 'y': 2}
# Такого атрибута не существует

