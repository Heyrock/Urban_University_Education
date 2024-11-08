class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        # print(Vector.norm2(self.x, self.y)) # 5
        print(self.norm2(self.x, self.y)) # 5
        
    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(1, 2)
# v2 = Vector(1, 200)
print(Vector.get_coords(v)) # (1, 2)
print(v.get_coords())
# print(Vector.get_coords(v2)) # (0, 0)
print(Vector.validate(50)) # True
print(Vector.norm2(5, 6)) # 61

# чиста поржать
print(Vector.get_coords(Vector(7, 8))) # (7, 8)
print(Vector(7, 8).get_coords()) # (7, 8)