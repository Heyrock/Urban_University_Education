class Geom:
    # def get_pr(self):
    #     return -1
    def get_pr(self):
        raise NotImplementedError(
            'В дочернем классе должен быть переопределен метод get_pr()'
        )


class Rect(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_pr(self):
    #     return self.a + self.b + self.c


r1 = Rect(1, 2)
r2 = Rect(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

lst = [r1, r2, s1, s2, t1, t2]

for i in lst:
    try:
        print(i.get_pr())
    except NotImplementedError as exc:
        print(exc)

# 6
# 14
# 40
# 80
# В дочернем классе должен быть переопределен метод get_pr()
# В дочернем классе должен быть переопределен метод get_pr()