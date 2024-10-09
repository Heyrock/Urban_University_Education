# 1+3 1+4 1+9 1+19 2+3 2+8 2+18 3+7 3+17 4+6 4+16 5+15 6+14 7+13 8+12 9+11
# 13141911923282183731746416515614713812911

nums = 20
my_list = [i for i in range(3, nums + 1) if nums % i == 0]
print(f'my_list = {my_list}')
new_list = []

for i in range(1, nums // 2):
    for num in my_list:
        if i < (num + 1)// 2:
            print(f'{i}+{num - i}')
            new_list.append(i)
            new_list.append(num - i)
    print()


print(''.join(map(str, new_list)))
print('13141911923282183731746416515614713812911')

# 1314191192  82183731746416515614713812911
# 13141911923282183731746416515614713812911