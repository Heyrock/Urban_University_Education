class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, и мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У {self.name} сегодня день рождения, исполнилось {self.age}')

    def __str__(self):
        return f'{self.name} к вашим услугам!'

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __bool__(self):
        return bool(self.age)

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):
        print(f'{self.name} ушел')


den = Human(name='Денис', age=22)
max = Human(name='Максим', age=23)
# print(den) # Денис к вашим услугам!
# print(den.__str__()) # Денис к вашим услугам!
# print(den.__repr__()) # <class '__main__.Human'>: Денис
print(den.age + max.age)
print(den + max)


