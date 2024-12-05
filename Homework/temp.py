def all_variants(text):
    for i in range(3 + 1):
        for j in range(3 - i + 1):
            if text[j:j + i]:
                yield text[j:j + i]


a = all_variants("abc")
for i in a:
    print(i, end=' ')
# a b c ab bc abc