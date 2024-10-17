def calculate_structure_sum_iter(user_list: list):
    new_list = []
    count = 0
    while user_list:
        current = user_list.pop(0)
        if isinstance(current, (str, int)):
            new_list.append(current)

        elif isinstance(current, (list, tuple, set)):
            user_list.extend(current)

        elif isinstance(current, dict):
            user_list.extend(current.keys())
            user_list.extend(current.values())

    for i in new_list:
        if isinstance(i, int):
            count += i
        else:
            count += len(i)

    return count


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum_iter(data_structure)

print(result)