from functools import reduce
from datetime import datetime

x = [1, 2, 3]
start = datetime.now()
reduce(sum, (x ** 0.5 for x in range(10 ** 7)))

print(datetime.now() - start)
