class Clock:
    __DAY = 86400 # кол-во секунд в сутках

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')

        # Считаем кол-во секунд в текущем дне от 00:00
        self.sc = seconds % self.__DAY

    @staticmethod
    def __verify_data(other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Правый операнд должен быть числом или Clock')
        # sc = other if isinstance(other, int) else other.sc
        # return sc
        return other if isinstance(other, int) else other.sc

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.sc == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.sc == sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.sc >= sc


c1 = Clock(1000)
c2 = Clock(2000)
# print(c1 == c2)
# # True
# print(c1 == 1000)
# # True
# print(c1 != 1000)
# # False
print(c1 <= 900)
# False
print(c1 <= c2)
# True