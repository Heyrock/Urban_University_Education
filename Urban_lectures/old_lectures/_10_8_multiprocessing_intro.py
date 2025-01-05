# потоки

import multiprocessing
import threading
import time
import operator


counter = 0

def first_worker(n):
    global counter
    for i in range(n):
        j = operator.iadd(counter, 1)
        counter = j
        time.sleep(0.1)
    print('Первый рабочий изменил счетчик, теперь -', counter)



def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(0.1)
    print('Второй рабочий изменил счетчик, теперь -', counter)


th1 = threading.Thread(target=first_worker, args=(10, ))
th2 = threading.Thread(target=second_worker, args=(5, ))
th1.start()
th2.start()
# Второй рабочий изменил счетчик, теперь - 11
# Первый рабочий изменил счетчик, теперь - 15

# процессы

counter = 0

def first_worker(n):
    global counter
    for i in range(n):
        j = operator.iadd(counter, 1)
        counter = j
        time.sleep(0.1)
    print('Первый рабочий изменил счетчик, теперь -', counter)


def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(0.1)
    print('Второй рабочий изменил счетчик, теперь -', counter)


if __name__ == '__main__':
    pr1 = multiprocessing.Process(target=first_worker, args=(10,))
    pr2 = multiprocessing.Process(target=second_worker, args=(5,))
    pr1.start()
    pr2.start()

# Первый рабочий изменил счетчик, теперь - 10
# Второй рабочий изменил счетчик, теперь - 15
