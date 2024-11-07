class First:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Second:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Joint:
    def __init__(self):
        self.firsts = []
        self.seconds = []

    def add_firsts(self, item):
        self.firsts.append(item)

    def add_seconds(self, item):
        self.seconds.append(item)

    def data(self):
        print(self.firsts)
        print(self.seconds)

    def __contains__(self, item):
        return lambda item: item in (
            [i.a for i in self.firsts],
            [i.b for i in self.firsts]
        )


first = First(1, 2, 3)
first2 = First(4, 5, 6)
second = Second(10, 20, 30)
second2 = Second(40, 50, 60)
joint = Joint()
joint.add_firsts(first)
joint.add_firsts(first2)
joint.add_seconds(second)
joint.add_seconds(second2)
joint.data()
print('jg' in joint)
print(2 in joint)
