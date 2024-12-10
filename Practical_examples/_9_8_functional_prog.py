animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

# 1. Написать функцию, которая возвращает функцию повторения первых двух символов n раз
def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal
    return repeat


# test_1 = gen_repeat(1)
# test_2 = gen_repeat(2)
# print(test_1(animal))
# print(test_2(animal))
#
# print(gen_repeat(1)(animal))
# print(gen_repeat(2)(animal))


# 2. Создать массив функций и применить все функции поочередно к аргументу
repetitions = [gen_repeat(n) for n in range(1, 4)]
result = [func(animal) for func in repetitions]
print(*result)
# ми-мишка ми-ми-мишка ми-ми-ми-мишка

result = [func(animal) for func in [gen_repeat(n) for n in range(1, 4)]]
print(*result)
# ми-мишка ми-ми-мишка ми-ми-ми-мишка



# 3. Применить все функции поочередно к массиву аргументов
fin_result = (func(a) for func in repetitions for a in animals)
for i in fin_result:
    print(i)
# за-зайка
# ми-мишка
# бе-бегемотик
# за-за-зайка
# ми-ми-мишка
# бе-бе-бегемотик
# за-за-за-зайка
# ми-ми-ми-мишка
# бе-бе-бе-бегемотик


fin_result = (func(a) for a in animals for func in repetitions)
for i in fin_result:
    print(i)
# за-зайка
# за-за-зайка
# за-за-за-зайка
# ми-мишка
# ми-ми-мишка
# ми-ми-ми-мишка
# бе-бегемотик
# бе-бе-бегемотик
# бе-бе-бе-бегемотик