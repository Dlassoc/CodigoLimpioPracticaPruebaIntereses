import unittest
from Modulos.Logical import amortization_plan, exercise, amortization_plan_with_extra_payment_file


class MyTestCase(unittest.TestCase):

    def test_payment_1(self):
        product_value = 200000
        interest_rate = 0.031
        installments = 36
        total_interest_value = 134726.53
        result = exercise.MonthlyInstallment.calculate_monthly_installment(product_value, interest_rate, installments)
        self.assertAlmostEqual(total_interest_value, result, places=2)

    def test_payment_2(self):
        product_value = 850000
        interest_rate = 0.034
        installments = 24
        total_interest_value = 407059.97
        result = exercise.MonthlyInstallment.calculate_monthly_installment(product_value, interest_rate, installments)
        self.assertAlmostEqual(total_interest_value, result, places=2)

    def test_payment_3(self):
        product_value = 480000
        interest_rate = 0
        installments = 48
        total_interest_value = 0
        result = exercise.MonthlyInstallment.calculate_monthly_installment(product_value, interest_rate, installments)
        self.assertAlmostEqual(total_interest_value, result, places=2)

    def test_payment_4(self):
        product_value = 480000
        interest_rate = 0.125
        installments = 48
        try:
            exercise.MonthlyInstallment.calculate_monthly_installment(product_value, interest_rate, installments)
        except exercise.ValueError as e:
            self.assertEqual(str(e), "The value exceeds optimal interest rates")

    def test_payment_5(self):
        product_value = 0
        interest_rate = 0.024
        installments = 60
        try:
            exercise.MonthlyInstallment.calculate_monthly_installment(product_value, interest_rate, installments)
        except exercise.ValueError as e:
            self.assertEqual(str(e), "The product value must be greater than 0")

    def test_payment_6(self):
        product_value = 50000
        interest_rate = 0.01
        installments = -10
        try:
            exercise.MonthlyInstallment.calculate_monthly_installment(product_value, interest_rate, installments)
        except exercise.ValueError as e:
            self.assertEqual(str(e), "Installments cannot be negative")

    def test_amortization_plan(self):
        monthly_payment = 9297.96
        product_value = 200000
        installments = 36
        interest_rate = 0.031
        try:
            plan = amortization_plan.amortization_plan_logic(monthly_payment, product_value, installments, interest_rate)
        except exercise.ValueError as e:
           self.assertEqual(str(e), "Installments cannot be negative")

    def test_amortization_plan_2(self):
        monthly_payment = 10000
        product_value = 480000
        installments = 48
        interest_rate = 0
        try:
            plan = amortization_plan.amortization_plan_logic(monthly_payment, product_value, installments, interest_rate)
        except exercise.ValueError as e:
            self.assertEqual(str(e), "Installments cannot be negative")

    def test_amortization_plan_extra_1(self):
        monthly_payment = 9297.96
        product_value = 200000
        installments = 27
        interest_rate = 0.031
        extra_payment = 53000
        extra_payment_month = 10
        plan = amortization_plan_with_extra_payment_file.amortization_plan_with_extra_payment(monthly_payment,
                                                                                              product_value,
                                                                                              installments,
                                                                                              interest_rate,
                                                                                              extra_payment,
                                                                                              extra_payment_month)
        self.assertEqual(len(plan), installments)

    def test_amortization_plan_extra_2(self):
        monthly_payment = 52377.50
        product_value = 850000.00
        installments = 23
        interest_rate = 0.034
        extra_payment = 90000
        extra_payment_month = 5
        plan = amortization_plan_with_extra_payment_file.amortization_plan_with_extra_payment(monthly_payment,
                                                                                              product_value,
                                                                                              installments,
                                                                                              interest_rate,
                                                                                              extra_payment,
                                                                                              extra_payment_month)
        self.assertEqual(len(plan), installments)

    def test_amortization_plan_extra_3(self):
        monthly_payment = 52377
        product_value = 850000
        installments = 23
        interest_rate = 0.034
        extra_payment = 90000
        extra_payment_month = 10
        try:
            plan = amortization_plan_with_extra_payment_file.amortization_plan_with_extra_payment(monthly_payment, product_value, installments, interest_rate, extra_payment, extra_payment_month)
        except exercise.ValueError as e:
            self.assertEqual(str(e), "The extra payment must be greater than the base monthly payment")

    def test_amortization_plan_extra_4(self):
        monthly_payment = 52377.50
        product_value = 850000.00
        installments = 23
        interest_rate = 0.034
        extra_payment = 90000
        extra_payment_month = 22
        try:
            plan = amortization_plan_with_extra_payment_file.amortization_plan_with_extra_payment(monthly_payment, product_value, installments, interest_rate, extra_payment, extra_payment_month)
        except exercise.ValueError as e:
            self.assertEqual(str(e), "The extra payment must be greater than the base monthly payment")

if __name__ == '__main__':
    unittest.main()
