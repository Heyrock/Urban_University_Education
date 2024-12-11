import threading
import time

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
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')


thread_1 = MyThread('thread_1', 5, 1)
thread_2 = MyThread('thread_2', 3, 0.5)
thread_1.start()
thread_2.start()
# Поток thread_1 запущен
# Поток thread_2 запущен
# thread_2 - Wed Dec 11 12:29:45 2024
# thread_1 - Wed Dec 11 12:29:46 2024
# thread_2 - Wed Dec 11 12:29:46 2024
# thread_2 - Wed Dec 11 12:29:46 2024
# Поток thread_2 завершен
# thread_1 - Wed Dec 11 12:29:47 2024
# thread_1 - Wed Dec 11 12:29:48 2024
# thread_1 - Wed Dec 11 12:29:49 2024
# thread_1 - Wed Dec 11 12:29:50 2024
# Поток thread_1 завершен