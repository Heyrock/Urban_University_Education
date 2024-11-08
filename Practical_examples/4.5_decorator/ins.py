from Practical_examples.decorator import bubble_sort, selection_sort, insertion_sort

# [print(*list(map(int, input('Введите числа через пробел: ').split())))
#  for _ in range(int(input('Введите количество списков чисел: ')))]

data_1 = list(map(int, input('Введите числа через пробел: ').split()))
data_2 = list(map(int, input('Введите числа через пробел: ').split()))
data_3 = list(map(int, input('Введите числа через пробел: ').split()))
print()
print('Сортировка пузырьком: ', *bubble_sort(data_1), '\n')
print('Сортировка выбором:   ', *selection_sort(data_2), '\n')
print('Сортировка вставкой:  ', *insertion_sort(data_3), '\n')
