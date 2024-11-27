# Дополнительное практическое задание по модулю: "Подробнее о функциях."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного
# уровня сложности
#
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
#
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда
# по утру сами путаются в том, что намудрили вчера вечером.
#
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы
# (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и
# выглядел следующим образом:
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение
# для подсчёта суммы всех чисел и длин всех строк?"
#
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре
# (списку, словарю и т.д.) по-разному.
#
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам -
# универсального решения для таких структур он не нашёл.
#
# Помогите сокурснику осуществить его задумку.
#
# Что должно быть подсчитано:
# 1. Все числа (не важно, являются они ключами или значениями или ещё чем-то).
# 2. Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
#
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
#
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
#
# print(result)
#
# Выходные данные (консоль):
# 99
#
# Примечания (рекомендации):
# 1. Весь подсчёт должен выполняться одним вызовом функции.
# 2. Рекомендуется применить рекурсивный вызов функции, для каждой
# внутренней структуры.
# 3. Т.к. каждая структура может содержать в себе ещё несколько элементов,
# можно использовать параметр *args
# 4. Для определения типа данного используйте функцию isinstance.

# ВАРИАНТ ЧЕРЕЗ ИТЕРАТИВНУЮ ФУНКЦИЮ
# def calculate_structure_sum(user_list: list):
#     new_list = []
#     count = 0
#     while user_list:
#         current = user_list.pop(0)
#         if isinstance(current, (str, int, float)):
#             new_list.append(current)
#
#         elif isinstance(current, (list, tuple, set)):
#             user_list.extend(current)
#
#         elif isinstance(current, dict):
#             user_list.extend(current.keys())
#             user_list.extend(current.values())
#
#     for i in new_list:
#         if isinstance(i, (int, float)):
#             count += i
#         else:
#             count += len(i)
#
#     return count
#
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
#
# print(result)


# ВАРИАНТ ЧЕРЕЗ РЕКУРСИВНУЮ ФУНКЦИЮ
#
# ПРАВИЛЬНОЕ  ОПРЕДЕЛЕНИЕ ФУНКЦИИ ТУТ НЕ РАБОТАЕТ
# def calculate_structure_sum(user_list, new_list=None):
    # if new_list is None:
    #     new_list = []

# ТОЛЬКО ТАК, ПЕРЕПРОБОВАЛ ВСЁ
def calculate_structure_sum(user_list, new_list=[]):
    for item in user_list:
        if isinstance(item, (list, set, tuple)):
            calculate_structure_sum(item)
        elif isinstance(item, dict):
            item = item.items()
            calculate_structure_sum(item)
        else:
            new_list.append(item)
    count = 0

    for i in new_list:
        count += len(i) if isinstance(i, str) else i
    return count


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))


