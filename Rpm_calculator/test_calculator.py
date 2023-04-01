import unittest
from rpn_calculator import RPNCalculator

class TestRPNCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = RPNCalculator()

    def test_single_digit_addition(self):
        result = self.calculator.evaluate('2 3 +')
        self.assertEqual(result, 5)

    def test_single_digit_subtraction(self):
        result = self.calculator.evaluate('5 3 -')
        self.assertEqual(result, 2)

    def test_single_digit_multiplication(self):
        result = self.calculator.evaluate('2 3 *')
        self.assertEqual(result, 6)

    def test_single_digit_division(self):
        result = self.calculator.evaluate('6 3 /')
        self.assertEqual(result, 2)

    def test_multiple_operations(self):
        result = self.calculator.evaluate('2 3 * 5 +')
        self.assertEqual(result, 11)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate('4 0 /')

if __name__ == '__main__':
    unittest.main()
