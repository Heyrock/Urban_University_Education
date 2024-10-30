def foo(a, *args, b):
    print(a, args, b)

tup = (1, 2, 3, 4)

foo(*tup)
# 1 (2, 3, 4) 35

foo(1, *tup, b=35)
# 1 (1, 2, 3, 4) 35

foo(1, 5, *tup, b=35)
# 1 (5, 1, 2, 3, 4) 35

foo(1, *tup, b=35)
# 1 (1, 2, 3, 4) 35

foo(1, b=35)
# 1 () 35

foo(1, 2, b=35)
# 1 (2,) 35

foo(1)
# TypeError: foo() missing 1 required keyword-only argument: 'b'

foo(1, 2, 3)
# TypeError: foo() missing 1 required keyword-only argument: 'b'