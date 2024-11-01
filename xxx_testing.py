class CustomNumber:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        if isinstance(other, CustomNumber):
            return self.value + other.value
        else:
            return self.value + other
    def __radd__(self, other):
        return self.__add__(other)


a = CustomNumber(5)
b = CustomNumber(10)
print(a + b) # Вывод: 15
print(a + 2) # Вывод: 7
print(3 + a) # Вывод: 8