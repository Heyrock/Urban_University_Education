from dis import dis


def say_hi():
    print('Привет! Я из модуля xxx_testing')

b = 10


def print_num():
    from random import randint
    print(randint(1, 10))


def main():
    a = 5

    def say_no():
        print('no')


if __name__ == '__main__':
    main()

# print_num()
# print(print_num())
dis(say_hi)
