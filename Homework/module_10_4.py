import threading
from queue import Queue
from random import randint
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # sleep(randint(3, 10))
        sleep(randint(1, 3))
        # sleep(1)
        print(f'{self.name}, EATING')


class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        for table, guest in zip(self.tables, guests):
            table.guest = guest
            table.guest.start()
            print(f'{guest.name} сел(-а) за стол номер {table.number}')

        for i in range(len(self.tables), len(guests)):
            self.queue.put(guests[i])
            print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        # while not self.queue.empty() or threading.current_thread().is_alive():
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest and not threading.current_thread().is_alive():
                # if table.guest:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)"')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                elif not self.queue.empty() and table.guest == None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    table.guest.start()
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) '
                          f'за стол номер {table.number}')


# Пример результата выполнения программы:
# Выполняемый код:

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
