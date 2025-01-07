import unittest
import _12_4_TestCase as file

calcTS = unittest.TestSuite()
# calcTS.addTest(unittest.makeSuite(file.CalcTest))

calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(file.CalcTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(file.NewCalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)

# test_add (_12_4_TestCase.CalcTest.test_add) ... skipped 'Не нужен'
# test_div (_12_4_TestCase.CalcTest.test_div) ... ok
# test_mul (_12_4_TestCase.CalcTest.test_mul) ... skipped 'Выпал 0'
# test_sub (_12_4_TestCase.CalcTest.test_sub) ... skipped 'Выпал 1'
# test_pow (_12_4_TestCase.NewCalcTest.test_pow) ... ok
# test_sqrt (_12_4_TestCase.NewCalcTest.test_sqrt) ... ok
#
# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s
#
# OK