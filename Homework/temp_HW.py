a = 10
x = 15
d = 37

fe = a - x % a
print(f'fe - {fe}')
gh = (x + d) % a
print(f'gh - {gh}')
eg = (d - fe - gh)
# print(f'eg - {eg}')

result = (eg // a - 1) + (fe + gh) // a + 1
# print(f'количество клеток {result}')

oh = x + d
print(oh // a)
print(x // a)
og = oh - gh
print(og // a)
print(eg // a)