def my_func(lst):
    count = 0
    for i in lst:
        if isinstance(i, (list, set, tuple)):
            print(i)
            my_func(list(i))
        elif isinstance(i, dict):
            print(i)
            my_func(list(i.items()))
        elif isinstance(i, str):
            print(f'adding len({i}) = {len(i)}')
            count += len(i)
            print(f'count = {count}')
        elif isinstance(i, int):
            print(f'adding {i}')
            count += i
            print(f'count = {count}')

    return count


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(my_func(data_structure))
