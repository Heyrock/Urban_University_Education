# Цель: освоить методы, которые содержит класс TestCase.
#
# Задача:
#
# В первую очередь скачайте исходный код, который нужно обложить тестами с
# GitHub. (Можно скопировать)
#
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner
# и новый класс Tournament.
#
# Изменения в классе Runner:
#
# 1. Появился атрибут speed для определения скорости бегуна.
# 2. Метод __eq__ для сравнивания имён бегунов.
# 3. Переопределены методы run и walk, теперь изменение дистанции зависит от
# скорости.
#
# Класс Tournament представляет собой класс соревнований, где есть дистанция,
# которую нужно пробежать и список участников.
# Также присутствует метод start, который реализует логику бега по предложенной
# дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase.
# В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results.
# Это словарь в который будут сохраняться результаты всех тестов.
#
# setUp - метод, где создаются 3 объекта:
#
# 1. Бегун по имени Усэйн, со скоростью 10.
# 2. Бегун по имени Андрей, со скоростью 9.
# 3. Бегун по имени Ник, со скоростью 3.
#
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Также методы тестирования забегов, в которых создаётся объект Tournament
# на дистанцию 90. У объекта класса Tournament запускается метод start, который
# возвращает словарь в переменную all_results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект
# из all_results (брать по наибольшему ключу) и предполагаемое имя последнего
# бегуна.
#
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект
# Tournament соблюсти):
#
# 1. Усэйн и Ник
# 2. Андрей и Ник
# 3. Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.
#
#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена
# логическая ошибка. В результате его работы бегун с меньшей скоростью может
# пробежать некоторые дистанции быстрее, чем бегун с большей.
#
# Попробуйте решить эту проблему и обложить дополнительными тестами.
#
# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
#
# Примечания:
#
# 1. Ваш код может отличаться от строгой последовательности описанной в задании.
# Главное - схожая логика работы тестов и наличие всех перечисленных
# переопределённых методов из класса TestCase.

import module_12_3_to_be_checked as file
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results = {}

    def setUp(self) -> None:
        self.usain = file.Runner(name='Усэйн', speed=10)
        self.andrey = file.Runner(name='Андрей', speed=9)
        self.nick = file.Runner(name='Ник', speed=3)

    @classmethod
    def tearDownClass(cls) -> None:
        for value in cls.all_results.values():
            print({item: val.name for item, val in value.items()})

    def test_1(self):
        participants = [self.usain, self.nick]
        tournament = file.Tournament(90, *participants)
        self.all_results['Тест 1'] = tournament.start()
        self.assertTrue((self.all_results['Тест 1'][2]), 'Ник')

    def test_2(self):
        participants = [self.andrey, self.nick]
        tournament = file.Tournament(90, *participants)
        self.all_results['Тест 2'] = tournament.start()
        self.assertTrue((self.all_results['Тест 2'][2]), 'Ник')

    def test_3(self):
        participants = [self.usain, self.andrey, self.nick]
        tournament = file.Tournament(90, *participants)
        self.all_results['Тест 3'] = tournament.start()
        self.assertTrue((self.all_results['Тест 3'][3]), 'Ник')


if __name__ == '__main__':
    unittest.main()

