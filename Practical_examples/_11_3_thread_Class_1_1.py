# threading Classes
import random
import time
from threading import Thread
import queue
import operator

class Bulka(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self) -> None:
        while True:
            time.sleep(0.2)
            if random.random() > 0.9:
                self.queue.put('подгорелая булка')
                # print('добавил подгорелую булку')
            else:
                self.queue.put('нормальная булка')
                # print('добавил нормальную булку')


class Kotleta(Thread):
    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count

    def run(self) -> None:
        while self.count:
            print('на подносе булок:', queue.qsize())
            bulka = self.queue.get(timeout=10)
            if bulka == 'нормальная булка':
                time.sleep(0.3)
                x = operator.isub(self.count, 1)
                self.count = x
            print('осталось приготовить бургеров', self.count)


queue = queue.Queue(maxsize=2)

bulka = Bulka(queue=queue)
kotleta = Kotleta(queue=queue, count=5)

bulka.start()
kotleta.start()

bulka.join()
kotleta.join()

# на подносе булок: 0
# осталось приготовить бургеров 4
# на подносе булок: 1
# осталось приготовить бургеров 4
# на подносе булок: 0
# осталось приготовить бургеров 3
# на подносе булок: 1
# осталось приготовить бургеров 2
# на подносе булок: 2
# осталось приготовить бургеров 1
# на подносе булок: 2
# осталось приготовить бургеров 0