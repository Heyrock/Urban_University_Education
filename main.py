# name = input('Введите ваше имя: ')
# if name == 'xxx':
#     print('Панки, хой!')
# else:
#     print(f'Дратути, {name}!')
#
number = int(input('Введите число: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0:
    print('Fizz')
else:
    print('Wrong number')