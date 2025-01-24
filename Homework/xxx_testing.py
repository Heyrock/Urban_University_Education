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


logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests_1.log',
    encoding='UTF-8',
    format='%(asctime)s | %(levelname)s | %(message)s',
)

if __name__ == '__main__':
    unittest.main()
