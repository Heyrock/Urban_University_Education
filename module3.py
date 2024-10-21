# from modules.module2 import say_hi, print_num
from modules.module2 import say_hi
import modules.module1
import modules.module2

# print(say_hi)
print(say_hi())
print(modules.module1.sh)

# Я в __init__ пакета modules
# Я в модуле1
# Привет! Я из модуля module2
# None
# <function say_hi at 0x000001AA07659DA0>