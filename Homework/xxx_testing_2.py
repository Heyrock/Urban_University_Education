import itertools

list_2 = itertools.combinations([3, 2, 1], 4)
print(list(list_2))  # [(3, 2, 1)]
list_2 = itertools.combinations_with_replacement([3, 2, 1], 4)
print(list(list_2))  
# [(3, 3, 3), (3, 3, 2), (3, 3, 1), (3, 2, 2), (3, 2, 1), (3, 1, 1), (2, 2, 2), (2, 2, 1), (2, 1, 1), (1, 1, 1)]