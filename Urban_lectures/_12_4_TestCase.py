import _12_1_calculator as calc
import unittest
import random

class CalcTest(unittest.TestCase):
    @unittest.skip(reason='Не нужен')
    def test_add(self):
        self.assertEqual(first=calc.add(a=1, b=2), second=3)

    @unittest.skipIf(
        condition=random.choice((0, 1)),
        reason='Выпал 1'
    )
    def test_sub(self):
        self.assertEqual(first=calc.sub(a=1, b=2), second=-1)

    @unittest.skipUnless(
        condition=random.choice((0, 1)),
        reason='Выпал 0'
    )
    def test_mul(self):
        self.assertEqual(first=calc.mul(a=3, b=2), second=6)

    def test_div(self):
        self.assertEqual(first=calc.div(a=10, b=2), second=5)


class NewCalcTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(first=calc.sqrt(a=4), second=2)

    def test_pow(self):
        self.assertEqual(first=calc.pow(a=3, b=3), second=27)


if __name__ == '__main__':
    unittest.main()
