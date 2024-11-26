class Clock:
    __DAY = 86400 # кол-во секунд в сутках

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')

        # Считаем кол-во секунд в текущем дне от 00:00
        self.sc = seconds % self.__DAY

    def get_time(self):
        s = self.sc % 60
        m = (self.sc // 60) % 60
        h = (self.sc // 3660) % 24
        return f'{self.__get_formatted(h)}:' \
               f'{self.__get_formatted(m)}:' \
               f'{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть числом или Clock')
        sc = other
        if isinstance(other, Clock):
            sc = other.sc
        return Clock(self.sc + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть числом или Clock')
        sc = other
        if isinstance(other, Clock):
            sc = other.sc
        self.sc += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
# c1.sc += 100
# c1 = 100 + c1
c1 += 100

print(c1.get_time())

# c3 = c2 + c1
# print(c3.get_time())
# 00:18:20
