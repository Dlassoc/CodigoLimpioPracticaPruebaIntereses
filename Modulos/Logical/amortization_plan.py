from tabulate import tabulate
from decimal import Decimal, ROUND_HALF_UP


def amortization_plan_logic(monthly_payment: float, product_value: float, installments: int,
                            interest_rate: float) -> list:
    amortization_table = []  # Initialize an empty list to store the amortization table.

    remaining_balance = Decimal(
        str(product_value))  # Convert the product value to a Decimal and initialize the remaining balance.

    month = 0  # Initialize the month counter.

    while remaining_balance > 0:
        month += 1  # Increment the month.

        actual_payment = Decimal(str(monthly_payment))  # Convert the monthly payment to a Decimal.

        # Calculate interest and principal payments for the current month.
        interest_payment = remaining_balance * Decimal(str(interest_rate))
        principal_payment = actual_payment - interest_payment

        if principal_payment > remaining_balance:
            principal_payment = remaining_balance  # Ensure principal payment doesn't exceed remaining balance.

        remaining_balance -= principal_payment  # Update the remaining balance.

        # Create a list with payment information for the current month and add it to the amortization table.
        payment_info = [
            month,
            "{:.2f}".format(remaining_balance.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(actual_payment.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(interest_payment.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(principal_payment.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(remaining_balance.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
        ]
        amortization_table.append(payment_info)  # Add the payment information to the amortization table.

    headers = ["Month", "Initial Balance", "Monthly Payment", "Interest", "Principal", "Remaining Balance"]
    print(tabulate(amortization_table, headers=headers, tablefmt="simple"))  # Display the amortization table.

    return amortization_table  # Return the amortization table.
