# list_ = [1, 2, 3, 4, 5, 6, 7, 8]
# tuple_ = (1, 2, 3, 4, 5, 6, 7, 8)
# print(list_.__sizeof__())  # 104
# print(tuple_.__sizeof__())  # 88
#
# tuple_2 = ([1, 2, 3], 'a', 'b')
# tuple_2[0].append(4)
# print(tuple_2)  # ([1, 2, 3, 4], 'a', 'b')
# tuple_2[0][1] = 200
# print(tuple_2)  # ([1, 200, 3, 4], 'a', 'b')
#

tuple_ = (4, 'string')
print(tuple_[1].replace('s', 'S'))  # String
print(tuple_)  # (4, 'string')
# ([1, 2, 3], 4, [1, 2, 3], 4, [1, 2, 3], 4)

