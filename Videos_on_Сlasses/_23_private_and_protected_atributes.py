class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self._name = Geom.__name

    def get_coords(self):
        return self.__x1, self.__y1

    def __verify_coord(self, coord):
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        # self.__verify_coord(x1) # нельзя
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill


r = Rect(0, 0, 10, 20)
# print(r.get_coords()) # (0, 0)
print(r._name) # Geom
# AttributeError: 'Rect' object has no attribute '_Rect__verify_coord'.
