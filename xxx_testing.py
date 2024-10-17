# def calculate_structure_sum(user_list, new_list=None):
#     if new_list is None:
#         new_list = []
def calculate_structure_sum(user_list, new_list=[]):
    for item in user_list:
        if isinstance(item, (list, set, tuple)):
            print(item)
            calculate_structure_sum(item)
        elif isinstance(item, dict):
            print(item)
            item = item.items()
            calculate_structure_sum(item)
        else:
            print(item)
            new_list.append(item)
    # print(new_list)
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


