my_string = input('Введите произвольный текст: ')
print()
length = len(my_string)
print(f'Количество знаков во введенном тексте: {length}')
print(f'Текст в верхнем регистре - "{my_string.upper()}"')
print(f'Текст в нижнем регистре - "{my_string.lower()}"')
print(f'Текст без пробелов - "{my_string.replace(" ", "")}"')
print(f'Первый символ текста - "{my_string[0]}"')
print(f'Последний символ текста - "{my_string[-1]}"')