# non-data descriptor
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


# data descriptor
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

    def __del__(self):
        pass


class Point3D:
    # интерфейсы взаимодействия
    x = Integer()
    y = Integer()
    z = Integer()
    rx = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # до применения дескрипторов
    # @classmethod
    # def verify_coord(cls, coord):
    #     if type(coord) != int:
    #         raise TypeError('Координата должна быть целым числом')

    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, x):
    #     self.verify_coord(coord=x)
    #     self._x = x
    #
    # @property
    # def y(self):
    #     return self._y
    #
    # @y.setter
    # def y(self, y):
    #     self.verify_coord(coord=y)
    #     self._y = y
    #
    # @property
    # def z(self):
    #     return self._z
    #
    # @z.setter
    # def z(self, z):
    #     self.verify_coord(coord=z)
    #     self._z = z


p = Point3D(1, 2, 3)
print(p.rx, p.__dict__)
