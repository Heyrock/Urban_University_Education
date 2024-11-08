class Human:
    head = True

    def say_hello(self):
        print('Hello!')


class Student(Human):
    head = False

    def about(self):
        print('Я - студент')
        

class Teacher(Human):
    pass


# human = Human()
student = Student()
print(student.head)
# Я - студент



# student.about()
# print(student.head) # True
# Student.head = False
# print(student.head) # False
# print(Human.__dict__)
# # 'head': True,
# print(Student.__dict__)
# 'head': False,
