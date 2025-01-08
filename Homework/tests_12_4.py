# Задача "Логирование бегунов":
#
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub.
# (Можно скопировать)
#
# Основное обновление - выбрасывание исключений, если передан неверный тип в name
# и если передано отрицательное значение в speed.
#
# Для решения этой задачи вам понадобится класс RunnerTest из предыдущей задачи.
#
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на
# следующие параметры:
#
# 1. Уровень - INFO
# 2. Режим - запись с заменой('w')
# 3. Название файла - runner_tests.log
# 3. Кодировка - UTF-8
# 4. Формат вывода - на своё усмотрение, обязательная информация:
# уровень логирования, сообщение логирования.
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
#
# test_walk:
#
# 1. Оберните основной код конструкцией try-except.
# 2. При создании объекта Runner передавайте отрицательное значение в speed.
# 3. В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# 4. В блоке except обработайте исключение соответствующего типа и логируйте
# его на уровне WARNING с сообщением "Неверная скорость для Runner".
#
# test_run:
#
# 1. Оберните основной код конструкцией try-except.
# 2. При создании объекта Runner передавайте что-то кроме строки в name.
# 3. В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# 4. В блоке except обработайте исключение соответствующего типа и логируйте его на
# уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
# Пример результата выполнения программы:
#
# Пример полученного файла логов runner_tests.log:

import logging
import unittest
import module_12_4_to_be_checked as file


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(
        condition=is_frozen,
        reason='Тесты в этом кейсе заморожены'
    )
    def test_walk(self):
        try:
            runner = file.Runner(
                name='Vasya',
                speed=-1
            )
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(msg='"test_walk" выполнен успешно')
        except:
            logging.warning(msg='Неверная скорость для Runner')

    @unittest.skipIf(
        condition=is_frozen,
        reason='Тесты в этом кейсе заморожены'
    )
    def test_run(self):
        try:
            runner = file.Runner(name=True)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(msg='"test_run" выполнен успешно')
        except:
            logging.warning(msg='Неверный тип данных для объекта Runner')

    @unittest.skipIf(
        condition=is_frozen,
        reason='Тесты в этом кейсе заморожены'
    )
    def test_challenge(self):
        runner_1 = file.Runner('Vasya')
        runner_2 = file.Runner('Petya')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(
            runner_1.distance,
            runner_2.distance,
        )


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig(
        level=logging.INFO,
        filemode='w',
        filename='runner_tests.log',
        encoding='UTF-8',
        format='%(asctime)s | %(levelname)s | %(message)s',
    )
