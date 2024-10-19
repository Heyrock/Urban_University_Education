def my_func(lst):
    count = 0
    if not lst:
        return 0

    elif isinstance(lst[0], (list, set, tuple)):
        lst[0] = list(lst[0])
        return my_func(lst[0]) + my_func(lst[1:])

    elif isinstance(lst[0], dict):
        lst[0] = list(lst[0].items())
        return my_func(lst[0]) + my_func(lst[1:])

    elif isinstance(lst[0], str):
        return len(lst[0]) + my_func(lst[1:])

    elif isinstance(lst[0], (int, float)):
        return lst[0] + my_func(lst[1:])
    else:
        return 0
    #     return count
    # count = 0
    #
    # for i in lst:
    #     count += len(i) if isinstance(i, str) else i
    # return count


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(my_func(data_structure))