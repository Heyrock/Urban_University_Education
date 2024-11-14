from string import ascii_letters

class Person:
    @staticmethod
    def alphabet():
        alpha = [i for i in range(ord('а'), ord('я') + 1)]
        alpha.insert(6, 1105)
        alpha_cyrillic = [chr(i) for i in alpha]
        return ''.join(alpha_cyrillic) + '-'

    S_RUS = alphabet()
    S_RUS_UPPER = S_RUS.upper()

    # def __init__(self, fio, age, ps, weight):
    #     self.verify_fio(fio)
    #     self.verify_age(age)
    #     self.verify_ps(ps)
    #     self.verify_weight(weight)
    #
    #     self.__fio = fio.split()
    #     self.__age = age
    #     self.__ps = ps
    #     self.__weight = weight

    def __init__(self, fio, age, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.age = age
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()

        if len(f) != 3:
            raise TypeError('Неверный формат записи')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) < 1:
                raise TypeError('A ФИО должен быть хотя бы один симвлол')
            if len(s.strip(letters)) != 0:
                raise TypeError('ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError('Возраст должен быть целым числом в диапазоне [14, 120]')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Вес должен быть вещественным числом от 20.0 и выше')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспортные данные должны быть строкой')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат данных')

        for p in s:
            if not p.isdigit():
                raise TypeError('Данные должны быть цифрами')

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__ps

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__ps = ps


p = Person('Ильиных Евгений Сергеевич', 47, '1234 567890', 93.0)
p.age = 15
print(p.age)
p.passport = '1212 343434'
p.weight = 92.9
print(p.__dict__)