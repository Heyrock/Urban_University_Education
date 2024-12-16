# 1 вариант - простой вариант

import threading as th
import time

def some_func():
    time.sleep(0.1)
    raise TypeError


def thread_func():
    try:
        some_func()
    except TypeError as e:
        print('Wow! Exception')


t1 = th.Thread(target=thread_func)
t2 = th.Thread(target=thread_func)

t1.start()
t2.start()

t1.join()
t2.join()

# Wow! Exception
# Wow! Exception

# 2 вариант - thread hooking

import threading as th
import time


def some_func():
    time.sleep(0.1)
    raise TypeError


def excepthook(args):
    print(args.thread.is_alive())
    print(args.thread.name)


th.excepthook = excepthook

t1 = th.Thread(target=some_func)
t2 = th.Thread(target=some_func)

t1.start()
t2.start()

t1.join()
t2.join()

# True
# Thread-1 (some_func)
# True
# Thread-2 (some_func)


# ------------------------------
# для сравнения добавили sys.hookexception

import threading as th
import time
import sys


def some_func():
    with lock:
        time.sleep(0.1)
        raise TypeError


def excepthook(args):
    print(args.thread.is_alive())
    print(args.thread.name)


def sys_excepthook(args, a, b):
    print('Handled')


th.excepthook = excepthook
sys.excepthook = sys_excepthook

t1 = th.Thread(target=some_func)
t2 = th.Thread(target=some_func)

lock = th.Lock()

t1.start()
t2.start()

t1.join()
t2.join()

raise Exception # for sys.excepthook

# True
# Thread-1 (some_func)
# True
# Thread-2 (some_func)
# Handled