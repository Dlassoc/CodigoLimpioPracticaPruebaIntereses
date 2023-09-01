from tabulate import tabulate
from decimal import Decimal, ROUND_HALF_UP


def amortization_plan_with_extra_payment(monthly_payment: float, product_value: float, installments: int,
                                         interest_rate: float,
                                         extra_payment: float, extra_payment_monthly: float):
    amortization_table = []
    remaining_balance = Decimal(str(product_value))

    month = 0
    while remaining_balance > 0 and month < installments:
        # This part of the code calculates interest and payments
        month += 1
        actual_payment = Decimal(str(monthly_payment))
        interest_payment = remaining_balance * Decimal(str(interest_rate))
        principal_payment = actual_payment - interest_payment

        # This part applies the extra payment if possible
        if month == extra_payment_monthly:
            if extra_payment >= actual_payment:
                principal_payment = extra_payment - interest_payment
            else:
                actual_payment = Decimal(str(extra_payment))
                principal_payment = extra_payment - interest_payment

        if principal_payment > remaining_balance:
            principal_payment = remaining_balance

        remaining_balance -= principal_payment

        payment_info = [
            month,
            "{:.2f}".format(remaining_balance.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(actual_payment.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(interest_payment.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(principal_payment.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(remaining_balance.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
        ]
        amortization_table.append(payment_info)

    headers = ["Month", "Initial Balance", "Monthly Payment", "Interest", "Principal", "Remaining Balance"]
    print(tabulate(amortization_table, headers=headers, tablefmt="simple"))
    return amortization_table
