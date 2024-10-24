# from package1.module1 import hello
# from package1.package2.package3.module1 import hello1
# from package1.package2.module2 import hello2
# from package1.package2.package3
from ..module1 import hello1
from .module2 import hello2
from .package3.module3 import hello3


def good_word(name):
    hello1(name)
    hello2(name)
    hello3(name)
    print('Ты - лучший,', name)


if __name__ == '__main__':
    good_word('Vasya')

# Привет, Урбан
# Ты - лучший, Урбан