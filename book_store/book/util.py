from decimal import Decimal


class TaxCalculator:
    TAX_UP_THREE_DAYS = None
    TAX_OVER_THREE_DAYS = None
    TAX_OVER_FIVE_DAYS = None

    def __init__(self, days_of_delay):
        self._days_of_delay = days_of_delay

    def _calculate_with_percentege(self, value, tax):
        return value * Decimal(tax)

    def _calculate_from_days_of_delay(self, value):
        if 0 < self._days_of_delay <= 3:
            return self._calculate_with_percentege(value, self.TAX_UP_THREE_DAYS)

        if 3 < self._days_of_delay <= 5:
            return self._calculate_with_percentege(value, self.TAX_OVER_THREE_DAYS)

        if self._days_of_delay > 5:
            return self._calculate_with_percentege(value, self.TAX_OVER_FIVE_DAYS)


class CalculatorPenalty(TaxCalculator):
    TAX_UP_THREE_DAYS = 0.03
    TAX_OVER_THREE_DAYS = 0.05
    TAX_OVER_FIVE_DAYS = 0.07

    def calculate(self, value):
        return self._calculate_from_days_of_delay(value)


class CalculatorInterestPerDay(TaxCalculator):
    TAX_UP_THREE_DAYS = 0.002
    TAX_OVER_THREE_DAYS = 0.004
    TAX_OVER_FIVE_DAYS = 0.006

    def calculate(self, value):
        return self._calculate_from_days_of_delay(value) * self._days_of_delay
