from Modulos.Logical.amortization_plan_with_extra_payment_file import amortization_plan_with_extra_payment


def extra_amortization_data():
    print("This program allows you to calculate the monthly installment for a credit card purchase")
    monthly_payment = float(input("Enter the monthly payment amount: "))
    product_value = float(input("Enter the product value: "))
    installments = int(input("Enter the number of installments to pay: "))
    interest_rate = float(input("Enter the interest rate for each installment (e.g., 0.031 for 3.1%): "))
    extra_payment = int(input("Enter the extra payment you will make: "))
    extra_payment_monthly = int(input("Enter the month in which the extra payment will be made: "))

    print(amortization_plan_with_extra_payment(monthly_payment, product_value, installments, interest_rate, extra_payment,extra_payment_monthly))


extra_amortization_data()
