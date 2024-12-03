class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        # если у класса есть такой метод, то его можно вызывать как функцию
        return self.n * x


nums = [1, 2, 3]
by_100500 = Multiplier(100500)
result = by_100500(42)
print(result)
# 4221000

# print(Multiplier(100500)(42))
# 4221000

print(list(map(by_100500, nums)))
# [100500, 201000, 301500]