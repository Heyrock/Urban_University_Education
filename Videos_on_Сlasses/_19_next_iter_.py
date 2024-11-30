# a = iter(range(5))
# print(next(a))
# print(next(a))
# print('пауза')
# print(next(a))

class FRange:
    def __init__(
            self,
            start=0.0,
            stop=0.0,
            step=1.0,
    ):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    # Получение значения текущей арифметической последовательности
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration('Тпруууу!')


# формирует таблицу значений
class FRange2D:
    def __init__(
            self,
            start=0.0,
            stop=0.0,
            step=1.0,
            rows=5
    ):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr2 = FRange2D(0, 2, 0.5, 4)

try:
    for row in fr2:
        for col in row:
            print(col, end='\t')
        print()

except StopIteration as exc:
    print(*exc.args)

# 0.0	0.5	1.0	1.5
# 0.0	0.5	1.0	1.5
# 0.0	0.5	1.0	1.5
# 0.0	0.5	1.0	1.5