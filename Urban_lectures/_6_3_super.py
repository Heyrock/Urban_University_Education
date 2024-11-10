class StudentGroup:
    def __init__(self, group):
        self.group = group
        print('Запуск StudentGroup')

    def about(self):
        print(f'{self.name} учится в группе {self.group}')


class Human:
    def __init__(self, name, group):
        super().__init__(group)
        self.name = name
        print('Запуск Human')
        super().about()

    def info(self):
        print(f'Привет, меня зовут {self.name}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        print('Запуск Student')
        self.info()


# human = Human('Старший', 2)
student = Student('Младший', 'MGLU', 'Группа 1')
# print(human.name)
# print(student.name, student.place)
# print(Student.mro())
# student.about()
# [<class '__main__.Student'>, <class '__main__.Human'>, <class '__main__.StudenGroup'>, <class 'object'>]

# Запуск StudentGroup
# Запуск Human
# Младший учится в группе 1
# Запуск Student
# Привет, меня зовут Младший