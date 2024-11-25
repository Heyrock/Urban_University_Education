try:
    truba = 1
except NameError as exc:
    print(exc)
else:
    print('Or else?')
finally:
    print('Вот такая вот фигня приключилась')
# Or else?
# Вот такая вот фигня приключилась