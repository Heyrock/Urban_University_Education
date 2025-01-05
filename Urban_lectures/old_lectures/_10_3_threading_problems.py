import threading

counter = 0
lock = threading.Lock()


def increment(name):
    global counter
    # lock.acquire()
    with lock:
        for _ in range(3):
            counter += 1
            print(name, counter, lock.locked())
    # lock.release()


# def decrement(name):
#     global counter
#     # lock.acquire()
#     with lock:
#         for _ in range(3):
#             counter -= 1
#             print(name, counter, lock.locked())
#     # lock.release()


def decrement(name):
    global counter
    try:
        lock.acquire()
        for _ in range(3):
            counter -= 1
            print(name, counter, lock.locked())
    except Exception:
        pass

    finally:
        lock.release()


th_1 = threading.Thread(target=increment, args=('th_1', ))
th_2 = threading.Thread(target=decrement, args=('th_2', ))
th_3 = threading.Thread(target=increment, args=('th_3', ))
th_4 = threading.Thread(target=decrement, args=('th_4', ))
th_1.start()
th_3.start()
th_2.start()
th_4.start()

#----------------------------------
# вариант из предыдущего урока с замком

import threading
import time

lock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        # super().__init__()
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    @staticmethod
    def timer(name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} - {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'Поток {self.name} запущен')
        # замок на вызов функции
        with lock:
            self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')


thread_1 = MyThread('thread_1', 5, 0.1)
thread_2 = MyThread('thread_2', 3, 0.05)
thread_1.start()
thread_2.start()

# Поток thread_1 запущен
# Поток thread_2 запущен
# thread_1 - Thu Dec 12 12:50:22 2024
# thread_1 - Thu Dec 12 12:50:22 2024
# thread_1 - Thu Dec 12 12:50:22 2024
# thread_1 - Thu Dec 12 12:50:22 2024
# thread_1 - Thu Dec 12 12:50:22 2024
# Поток thread_1 завершен
# thread_2 - Thu Dec 12 12:50:22 2024
# thread_2 - Thu Dec 12 12:50:22 2024
# thread_2 - Thu Dec 12 12:50:22 2024
# Поток thread_2 завершен