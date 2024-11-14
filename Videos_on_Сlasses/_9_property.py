class Person:
    def __init__(self, name, age):
        self.__name = name
        # self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    # age = property(get_age, set_age)

    # age = property()
    # age = age.setter(set_age)
    # age = age.getter(get_age)

    @age.deleter
    def age(self):
        del self.__age


p = Person('Sergey', 20)
# p.set_age(35)
# print(p.__dict__)
# {'_Person__name': 'Sergey', '_Person__age': 35}
# print(p.get_age())
# 35

# p.__dict__['age'] = 'age in object p'
# p.age = 35
# print(p.age, p.__dict__)
# 35 {'_Person__name': 'Sergey', '_Person__age': 35, 'age': 'age in object p'}

print(p.__dict__)
# {'_Person__name': 'Sergey', '_Person__age': 20}
p.age = 35
print(p.__dict__)
# {'_Person__name': 'Sergey', '_Person__age': 35}
del p.age
print(p.__dict__)
# {'_Person__name': 'Sergey'}
p.age = 13
print(p.__dict__)
# {'_Person__name': 'Sergey', '_Person__age': 13}

