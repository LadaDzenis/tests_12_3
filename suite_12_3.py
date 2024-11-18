import unittest
import tests_12_3


'''
Часть 1. TestSuit
'''
testST = unittest.TestSuite()

testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)

