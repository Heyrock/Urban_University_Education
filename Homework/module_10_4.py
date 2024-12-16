# Цель: Применить очереди в работе с потоками, используя класс Queue.
#
# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
#
# Создайте 3 класса: Table, Guest и Cafe.
#
# Класс Table:
# 1. Объекты этого класса должны создаваться следующим способом - Table(1)
# 2. Обладать атрибутами number - номер стола и guest - гость,
# который сидит за этим столом (по умолчанию None)
#
# Класс Guest:
# 1. Должен наследоваться от класса Thread (быть потоком).
# 2. Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# 3. Обладать атрибутом name - имя гостя.
# 4. Обладать методом run, где происходит ожидание случайным образом от
# 3 до 10 секунд.
#
# Класс Cafe:
# 1. Объекты этого класса должны создаваться следующим способом -
# Cafe(Table(1), Table(2),....)
# 2. Обладать атрибутами queue - очередь (объект класса Queue) и tables -
# столы в этом кафе (любая коллекция).
# 3. Обладать методами guest_arrival (прибытие гостей) и discuss_guests
# (обслужить гостей).
#
# Метод guest_arrival(self, *guests):
# 1. Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# 2. Далее, если есть свободный стол, то сажать гостя за стол
# (назначать столу guest), запускать поток гостя и выводить на экран строку
# "<имя гостя> сел(-а) за стол номер <номер стола>".
# 3. Если же свободных столов для посадки не осталось, то помещать гостя в
# очередь queue и выводить сообщение "<имя гостя> в очереди".
#
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# 1. Обслуживание должно происходить, пока очередь не пустая (метод empty)
# или хотя бы один стол занят.
# 2. Если за столом есть гость(поток) и гость(поток) закончил приём пищи
# (поток завершил работу - метод is_alive), то вывести строки
# "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и
# "Стол номер <номер стола> свободен".
# Также текущий стол освобождается (table.guest = None).
# 3. Если очередь ещё не пуста (метод empty) и один из столов освободился
# (None), то текущему столу присваивается гость, взятый из очереди (queue.get()).
# Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а)
# за стол номер <номер стола>"
# 4. Далее запустить поток этого гостя (start)
#
# Таким образом мы получаем 3 класса на основе которых имитируется
# работа кафе:
# 1. Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# 2. Guest - гость, поток, при запуске которого происходит задержка от
# 3 до 10 секунд.
# 3. Cafe - кафе, в котором есть определённое кол-во столов и происходит
# имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
#
#
# # Пример результата выполнения программы:
# # Выполняемый код:
#
# class Table:
# ...
#
# class Guest:
# ...
#
# class Cafe:
# ...
#
# # Создание столов
# tables = [Table(number) for number in range(1, 6)]
#
# # Имена гостей
# guests_names = [
# 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
# 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
# ]
#
# # Создание гостей
# guests = [Guest(name) for name in guests_names]
#
# # Заполнение кафе столами
# cafe = Cafe(*tables)
#
# # Приём гостей
# cafe.guest_arrival(*guests)
#
# # Обслуживание гостей
# cafe.discuss_guests()
#
#
# # Вывод на консоль (последовательность может меняться из-за случайного
# # время пребывания гостя):
#
# Maria сел(-а) за стол номер 1
# Oleg сел(-а) за стол номер 2
# Vakhtang сел(-а) за стол номер 3
# Sergey сел(-а) за стол номер 4
# Darya сел(-а) за стол номер 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Oleg покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
# .....
# Alexandra покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Pavel покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
#
# Примечания:
#
# 1. Для проверки значения на None используйте оператор is (table.guest is None).
# 2. Для добавления в очередь используйте метод put, для взятия - get.
# 3. Для проверки пустоты очереди используйте метод empty.
# 4. Для проверки выполнения потока в текущий момент используйте
# метод is_alive.

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
        sleep(randint(1, 3))
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

        # пока очередь не пустая или хотя бы один стол занят
        while not self.queue.empty() or \
                any(table.guest for table in self.tables if table.guest is not None):
        # while not self.queue.empty() or any(table.guest for table in self.tables):

            for table in self.tables:

                # Если за столом есть гость и гость закончил приём пищи
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)"')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                # Если очередь ещё не пуста и один из столов освободился
                elif not self.queue.empty() and table.guest is None:
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
