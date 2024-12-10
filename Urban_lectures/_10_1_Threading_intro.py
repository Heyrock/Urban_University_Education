import threading

print(threading.current_thread())
# <_MainThread(MainThread, started 10380)>

print(threading.enumerate())
# [<_MainThread(MainThread, started 1732)>]


# -------------------------------
import time


def func_1():
    for i in range(3):
        time.sleep(0.3)
        print(i, threading.current_thread())


def func_2(*args, **kwargs):
    for i in range(3):
        time.sleep(0.3)
        print(i, threading.current_thread())
        print(args)
        print(kwargs)


thread = threading.Thread(
    target=func_2,
    args=(1, 2, 3),
    kwargs={'a': 'x', 'b': 'y'}
)
thread.start()
func_1()

# 0 <Thread(Thread-1 (func_2), started 2592)>
# (1, 2, 3)0 <_MainThread(MainThread, started 17180)>
#
# {'a': 'x', 'b': 'y'}
# 1 <_MainThread(MainThread, started 17180)>
# 1 <Thread(Thread-1 (func_2), started 2592)>
# (1, 2, 3)
# {'a': 'x', 'b': 'y'}
# 2 <Thread(Thread-1 (func_2), started 2592)>
# (1, 2, 3)2 <_MainThread(MainThread, started 17180)>
#
# {'a': 'x', 'b': 'y'}

# ---------------------------

print(threading.current_thread().is_alive())

# ----------------------------

import threading
import time


def func_1():
    for i in range(3):
        time.sleep(0.3)
        print(i, threading.current_thread())


def func_2(*args, **kwargs):
    for i in range(3):
        time.sleep(0.3)
        print(i, threading.current_thread())


thread = threading.Thread(
    target=func_2,
    args=(1, 2, 3),
    kwargs={'a': 'x', 'b': 'y'}
)
thread.start()
thread.join()
print(thread.is_alive())
func_1()

# 0 <Thread(Thread-1 (func_2), started 2256)>
# 1 <Thread(Thread-1 (func_2), started 2256)>
# 2 <Thread(Thread-1 (func_2), started 2256)>
# False
# 0 <_MainThread(MainThread, started 9976)>
# 1 <_MainThread(MainThread, started 9976)>
# 2 <_MainThread(MainThread, started 9976)>

#-------------------------------

import threading
import time


def func_1():
    for i in range(3):
        time.sleep(0.3)
        print(i, threading.current_thread())


def func_2(*args, **kwargs):
    while True:
        time.sleep(0.3)
        print('sth', threading.current_thread())


thread = threading.Thread(
    target=func_2,
    daemon=True,
    args=(1, 2, 3),
    kwargs={'a': 'x', 'b': 'y'}
)
thread.start()
func_1()

# 0 <_MainThread(MainThread, started 6644)>
# sth <Thread(Thread-1 (func_2), started daemon 18772)>
# sth <Thread(Thread-1 (func_2), started daemon 18772)>
# 1 <_MainThread(MainThread, started 6644)>
# sth <Thread(Thread-1 (func_2), started daemon 18772)>
# 2 <_MainThread(MainThread, started 6644)>
