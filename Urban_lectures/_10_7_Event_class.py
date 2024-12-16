import threading
import time

def first_worker():
    print('Первый рабочий ПРИСТУПИЛ к своей задаче')
    event.wait()
    print('Первый рабочий ПРОДОЛЖИЛ выполнять свою задачу')
    time.sleep(1)
    print('Первый рабочий ЗАВЕРШИЛ выполнять свою задачу')


def second_worker():
    print('Второй рабочий ПРИСТУПИЛ к своей задаче')
    time.sleep(2)
    print('Второй рабочий ЗАВЕРШИЛ выполнять свою задачу')
    event.set()
    print(event.is_set())
    # True


event = threading.Event()

th1 = threading.Thread(target=first_worker)
th2 = threading.Thread(target=second_worker)
th1.start()
th2.start()
th1.join()
th2.join()

event.clear()
print(event.is_set())

# Первый рабочий ПРИСТУПИЛ к своей задаче
# Второй рабочий ПРИСТУПИЛ к своей задаче
# Второй рабочий ЗАВЕРШИЛ выполнять свою задачу
# True
# Первый рабочий ПРОДОЛЖИЛ выполнять свою задачу
# Первый рабочий ЗАВЕРШИЛ выполнять свою задачу
# False