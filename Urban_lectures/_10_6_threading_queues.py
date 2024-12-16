from queue import Queue
import time
import threading
from random import randint

# q = Queue()
# q.put(5)
# print(q.get(timeout=1))
# print('Конец программы')
# # 5
# # Конец программы

# ---------------------------------
# Пример использования FIFO
def getter(queue):
    # while True:
    while not queue.empty():
        time.sleep(0.5)
        item = queue.get()
        print(threading.current_thread(),
              'Взят элемент',
              item)

def getter_lock(queue):
    with lock:
        # while True:
        while not queue.empty():
            time.sleep(0.5)
            item = queue.get()
            print(threading.current_thread(),
                  'Взят элемент',
                  item)


lock = threading.Lock()
q = Queue(maxsize=10)
q.put(100)

thread_1 = threading.Thread(
    target=getter_lock,
    args=(q, ),
    daemon=True,
)
thread_lock = threading.Thread(
    target=getter,
    args=(q, ),
    daemon=True,
)
# thread_1.start()
thread_lock.start()

for i in range(10):
    time.sleep(0.2)
    q.put(i)
    print(threading.current_thread(),
          'Положен элемент',
          i)
