class Geom(object):
    pass


class Line(Geom):
    pass


print(Geom.__name__)
l = Line()
print(Line.mro())
print(issubclass(Line, Geom))
# True
print(issubclass(Line, object))
# True
print(isinstance(l, Geom))
# True


class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))


v = Vector([1, 2, 3])
print(v)
# 1 2 3