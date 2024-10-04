# num_9 = sum(int(i) for i in '1218273645')
# num_10 = sum(int(i) for i in '141923283746')
# num_11 = sum(int(i) for i in '11029384756')
# num_15 = sum(int(i) for i in '1214114232133124115106978')
# num_20 = sum(int(i) for i in '13141911923282183731746416515614713812911')
num_ref = sum(int(i) for i in '13141911923282183731746416515614713812911')
num_test = sum(int(i) for i in '13142319283746119218317416515614713812911')

# print(num_9) # 39
# print(num_10) # 50
# print(num_11) # 46
# print(num_15) # 73
# print(num_20) # 153

print(num_ref)
print(num_test)

num_1 = 9
summands = []


for j in range(1, (num_1 + 1) // 2):
    # print(j)
    summands.append((j, num_1 - j))


print(summands)