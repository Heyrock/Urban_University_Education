def all_variants(text):
    for i in range(len(text) + 1):
        for j in range(len(text) - i + 1):
            if text[j:j + i]:
                yield text[j:j + i]


a = all_variants("abc")
for i in a:
    print(i)

# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc