current_list = [[10, 6, 9], [0, 14, 16, 80], [8, 12, 30, 44]]
sorting_inner_lists = lambda cur_list: (sorted(i) for i in cur_list)
# print(list(sorting_inner_lists(current_list)))
# [[6, 9, 10], [0, 14, 16, 80], [8, 12, 30, 44]]

defining_second_largest = lambda cur_list, func: [y[-2] for y in func(cur_list)]
result = defining_second_largest(current_list, sorting_inner_lists)
print(result)

# [9, 16, 30]
