# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'Кот по имени {self.name}'
#
# cat = Cat('Васька')
# print(cat.__repr__())
# print(cat)
# # <class '__main__.Cat'>: Васька
# print(cat)
# # <__main__.Cat object at 0x000001E4BAB70450>
# # Кот по имени Васька

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(lambda x: abs(x), self.__coords))


p = Point(1, -2)
print(len(p))
print(abs(p))
# [1, 2]

