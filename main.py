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
        return self.name

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'{self.name} ушел')


eugen = Human('Евгений', 20)
max = Human(name='Максим', age=18)
eugen.birthday()
max.birthday()
print(eugen.__len__())
print(len(eugen))
print(eugen)
# del eugen
# input()
