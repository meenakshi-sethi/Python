import unittest 
from calculator_v2 import Calculator2 # module we want to test


class TestsCalculatorV2(unittest.TestCase): 
    def test_add_functionality(self):
        calc1 = Calculator2(10,30) # we crated instance of class calculator
        result = calc1.calc_add()
        self.assertEqual(result, 40)
    
    def test_add_functionality_with_one_negative_number(self):
        calc1 = Calculator2(10,-30)
        result = calc1.calc_add()
        self.assertEqual(result, -20)


if __name__ == "__main__":
    unittest.main(verbosity=2)