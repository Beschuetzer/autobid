# tests/runner.py
import unittest

# import your test modules
import test
import testgetSuitFromCardAsNumber

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test))
suite.addTests(loader.loadTestsFromModule(testgetSuitFromCardAsNumber))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)