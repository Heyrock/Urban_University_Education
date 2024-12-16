class GenerateInts: 
    def __init__(self, n):
    # конструктор принимает верхнюю границу диапазона
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.n:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print(next(GenerateInts(5)))
print(next(GenerateInts(5)))
print(next(GenerateInts(5)))
iter = GenerateInts(4)
print(next(iter))
print(next(iter))
print(next(iter))