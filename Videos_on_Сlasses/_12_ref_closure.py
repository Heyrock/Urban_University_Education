def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    return step


# c1 = counter(10)
# c2 = counter(0)
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())


def strip_string(strip_chars = ' '):
    def do_strip(string):
        return string.strip(strip_chars)
    return do_strip


str_ = '   fgfgfgf   '
f = strip_string()
print(strip_string()(str_))
print(f(str_))