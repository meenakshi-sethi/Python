import unittest # module that comes with python installation
import calculator # module we wrote

# We will create a simple class using unittest.TestCase and we will create method
class TestsCalculator(unittest.TestCase): 
    def test_add_functionality(self): # all the tests of the test must start with the prefix test. if we remove the test prefix method will not get executed
        result = calculator.calc_add(10,20)
        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)