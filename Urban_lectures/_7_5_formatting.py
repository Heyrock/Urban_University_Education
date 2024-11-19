# конкатенация
print('hello ' + 'world! ' + str(14))
# hello world! 14

# %-форматирование
print('My name is %s' % 'Eugene')
# My name is Eugene

print('My name is %s I am %s years old' % ('Eugene', 47))
# My name is Eugene I am 47 years old

print('My name is %(name)s I am %(age)s years old' %
      {'age': 47, 'name': 'Eugene'}
      )
# My name is Eugene I am 47 years old

# format method
print('My name is {}'.format('Eugene'))
# My name is Eugene

print('My name is {} I am {} years old'.format('Eugene', 47))
# My name is Eugene I am 47 years old

print('I am {0} and I am {1}, he is {2} and he is {1} too'.
      format('Eugene', 47, 'Roman'))
# I am Eugene and I am 47, he is Roman and he is 47 too

print(
    'My name is {name} I am {age} years old'.format(
        age=47, name='Eugene'
    )
)
# My name is Eugene I am 47 years old

# f-string
name = 'Eugene'
name_too = 'Roman'
print(
    f'I am {name} and I am {2 * 20 + 7}, he is {name_too} and he is {50 - 3} too'
)
# I am Eugene and I am 47, he is Roman and he is 47 too
