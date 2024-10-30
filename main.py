class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, и мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня сегодня день рождения, мне исполнилось {self.age}')


eugen = Human(name='Евгений', age=20)
max = Human(name='Максим', age=18)

