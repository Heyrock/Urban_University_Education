import re
import inspect

num = 42
x = str(type(num))
pattern_1 = re.compile('<class ')
pattern_2 = re.compile('>')
x = pattern_1.sub('', x)
x = pattern_2.sub('', x)
# print(x)

# <class 'int'>

class SomeClass:
    def __init__(self):
        self.name = 'Vasya'

    def some_func(self):
        print('hi')

# print(type(SomeClass.name))
# print(type(SomeClass.some_func))

instance = SomeClass()
# print(instance.__dict__)
num = 42
# print(inspect.getsourcefile(num))
print(__name__)

# print(path)
# print(inspect.getmodulename(path))