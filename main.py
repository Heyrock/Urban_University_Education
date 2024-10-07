def printer():
    global a
    a = 'five'
    c = 15
    print(a, c)


a = 5
b = 6

printer() # five 15
print(a) # 5
