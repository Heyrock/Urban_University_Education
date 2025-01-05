import _12_1_unit_testing_intro as calc
import unittest

class CalcTest(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp')

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    def tearDown(self) -> None:
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    # def test_add(self):
    #     """
    #     Test for add function in calculator
    #     :return:
    #     """
    #     self.assertEqual(calc.add(3, 4), 7)
    #
    # def test_sub(self):
    #     """
    #     Test for sub function in calculator
    #     :return:
    #     """
    #     self.assertEqual(calc.sub(3, 4), -1)

    def test_test(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 2)
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIsNone(None)
        self.assertIsNotNone(not None)
        self.assertIn('a', 'abc')
        self.assertNotIn('d', 'abc')
        self.assertIsInstance('a', str)
        self.assertNotIsInstance('a', int)
        self.assertRaises(ZeroDivisionError)
        self.assertAlmostEqual(0.0, 0.0)
        self.assertNotAlmostEqual(0.0, 0.1)
        self.assertGreater(2, 1)
        self.assertGreaterEqual(2, 1)
        self.assertLess(1, 2)
        self.assertLessEqual(1, 2)


if __name__ == '__main__':
    unittest.main()

# setUpClass
# setUp
# tearDown
# tearDownClass
#
# Ran 1 test in 0.006s
# OK
