def my_func(lst):
    count = 0
    if not lst:
        return lst

    elif isinstance(lst[0], (list, set, tuple)):
        lst[0] = list(lst[0])
        return my_func(lst[0]) + my_func(lst[1:])

    elif isinstance(lst[0], dict):
        lst[0] = list(lst[0].items())
        return my_func(lst[0]) + my_func(lst[1:])
    #
    # elif isinstance(lst[0], str):
    #     count += len(lst[0])
    #
    # elif isinstance(lst[0], int):
    #     count += lst[0]
    else:
        return lst[:1] + my_func(lst[1:])


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(my_func(data_structure))
# [1, 2, 3, 'a', 4, 'b', 5, 6, 'cube', 7, 'drum', 8, 'Hello', 2, 'Urban', 'Urban2', 35]