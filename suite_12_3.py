from unittest import TestSuite, TestLoader, TextTestRunner
import tests_12_1, tests_12_2

TS = TestSuite()
TS.addTest(TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
TS.addTest(TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = TextTestRunner(verbosity=2)
runner.run(TS)