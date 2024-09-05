import unittest
import test_12_4

tournement_TS = unittest.TestSuite()
tournement_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_4.TournamentTest))
tournement_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_4.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournement_TS)