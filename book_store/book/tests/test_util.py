import unittest
from decimal import *

from book.util import CalculatorPenalty, CalculatorInterestPerDay


class TestTaxCalculator(unittest.TestCase):

    def setUp(self):
        getcontext().prec = 3
        self.value = 300
        self.days_of_delay_three_percent = 3
        self.days_of_delay_five_percent = 5
        self.days_of_delay_seven_percent = 6

    def test_should_return_three_percent_penalty(self):
        calculator = CalculatorPenalty(self.days_of_delay_three_percent)
        value_penalty = calculator.calculate(self.value)
        self.assertEqual(value_penalty, 9.0)

    def test_should_return_five_percent_penalty(self):
        calculator = CalculatorPenalty(self.days_of_delay_five_percent)
        value_penalty = calculator.calculate(self.value)
        self.assertEqual(value_penalty, 15.0)

    def test_should_return_seven_percent_penalty(self):
        calculator = CalculatorPenalty(self.days_of_delay_seven_percent)
        value_penalty = calculator.calculate(self.value)
        self.assertEqual(value_penalty, 21.0)

    def test_should_return_interest_per_day_up_three_days(self):
        calculator = CalculatorInterestPerDay(self.days_of_delay_three_percent)
        value_interest_per_day = calculator.calculate(self.value)
        self.assertEqual(value_interest_per_day, Decimal('1.8'))
        self.assertIsInstance(value_interest_per_day, Decimal)

    def test_should_return_interest_per_day_over_three_days(self):
        calculator = CalculatorInterestPerDay(self.days_of_delay_five_percent)
        value_interest_per_day = calculator.calculate(self.value)
        self.assertEqual(value_interest_per_day, Decimal('6.0'))

    def test_should_return_interest_per_day_over_five_days(self):
        calculator = CalculatorInterestPerDay(self.days_of_delay_seven_percent)
        value_interest_per_day = calculator.calculate(self.value)
        self.assertEqual(value_interest_per_day, Decimal('10.80'))
