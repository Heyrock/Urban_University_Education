from dis import dis

print('Я в модуле2')

def say_hi():
    print('Привет! Я из модуля module2')

# b = 10


def print_num():
    from random import randint
    print(randint(1, 10))

def say_no():
        print('no')

def main():
    a = 5
    say_no()




if __name__ == '__main__':
    main()


# print_num()
# print(print_num())
# dis(say_hi)
