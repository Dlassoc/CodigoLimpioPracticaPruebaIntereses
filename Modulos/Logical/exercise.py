class ValueError(Exception):
    pass


class MonthlyInstallment:

    @staticmethod
    def calculate_monthly_installment(product_value: float, interest_rate: float, installments: int) -> float:
        if interest_rate == 0 or installments == 1:
            return 0.0
        elif interest_rate / 100 > 0.12:
            raise ValueError("The product value must be greater than 0")
        elif installments < 0:
            raise ValueError("Installments cannot be negative")
        else:
            monthly_payment = (product_value * interest_rate) / (1 - (1 + interest_rate) ** (-installments))
            return round(
                MonthlyInstallment.calculate_interests_before_payment(monthly_payment, product_value, installments), 2)

    @staticmethod
    def calculate_interests_before_payment(monthly_payment: float, product_value: float, installments: int) -> float:
        total_interests = (monthly_payment * installments) - product_value
        return total_interests
