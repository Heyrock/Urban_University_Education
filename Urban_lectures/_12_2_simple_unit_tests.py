import _12_1_calculator as calc
import unittest

class CalcTest(unittest.TestCase):
    def test_add(self):
        """
        Test for add function in calculator
        :return:
        """
        self.assertEqual(calc.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 4), -1)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 4), 12)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)


if __name__ == '__main__':
    # calctest = CalcTest()
    unittest.main()

# Ran 4 tests in 0.020s
#
# OK
