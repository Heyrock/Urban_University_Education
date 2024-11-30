class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('индекс должен быть целым неотрицательным числом')
        if key >= len(self.marks):
            # расширяем список на энное кол-во None
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('индекс должен быть целым неотрицательным числом')
        del self.marks[key]


s1 = Student('Sergey', [5, 5, 3, 2, 5])


try:
    s1[10] = 4
    # print(s1[3])
    del s1[2]
    print(s1.marks)
    print(s1[20])
except TypeError as exc:
    print(*exc.args)
except IndexError as exc:
    print(*exc.args)
# 2
# [5, 5, 2, 5, None, None, None, None, None, 4]
# Неверный индекс
