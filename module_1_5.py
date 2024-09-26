# Цель:
#
# Написать программу на языке Python, используя Pycharm, для работы с
# неизменяемыми и изменяемыми объектами.
#
# 1. В проекте, где вы решаете домашние задания, создайте модуль
# 'module_1_5.py' и напишите весь код в нём.
#
# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из
#   нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
#
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var.
#   Объясните, почему нельзя изменить значения элементов кортежа.
#
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из
#    нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.
#
import copy

print('Задание 2\n')
immutable_var = 1, '1', 'string', [2, 'string_2'], (4, 5, [6, 'string_3'])
print(immutable_var)

print('\nЗадание 3\n')
new_immutable_var = copy.deepcopy(immutable_var)
new_string = immutable_var[3][1].replace('2', '222')
old_list = immutable_var[3]
new_immutable_var[3][1] = new_string
new_list = new_immutable_var[3]

print(f"Я не могу изменить в списке '{old_list}' кортежа строку '{old_list[1]}' на '{new_string}',\n"
      f"поскольку строки, числа и кортежи неизменяемые.\n\n"
      f"Зато я могу поменять сам список, заменив один элемент на другой\n"
      f"и теперь список выглядит так: '{new_immutable_var[3]}',\n"
      f"а весь кортеж выглядит так:\n"
      f"'{new_immutable_var}'\n\n"
      f"В процессе узнал/вспомнил про новый подводный камень - списки меняются во всех версиях кортежа\n"
      f"Копировать нужно с умом (copy.deepcopy)...")

print('\nЗадание 4\n')

mutable_list = [1, 'a', (2, 3), [4, 5], True]
print(f'Исходный список: {mutable_list}')

mutable_list[0] = 2
mutable_list[1] = mutable_list[1].upper()
mutable_list[2] = mutable_list[2] * 2
mutable_list[3][0], mutable_list[3][1] = mutable_list[3][1], mutable_list[3][0]
mutable_list[4] = not mutable_list[4]

print(f'Измененный список: {mutable_list}')




