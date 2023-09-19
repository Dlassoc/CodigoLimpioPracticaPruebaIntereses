from Logical.exercise import MonthlyInstallment


def monthly_installment_data():
    print("This program allows you to calculate the monthly installment for a credit card purchase.")
    product_price = float(input("Enter the price of the product: "))
    interest_rate = float(input("Enter the credit card interest rate: "))
    installments = int(input("Number of installments to spread the purchase: "))
    print(MonthlyInstallment.calculate_monthly_installment(product_price, interest_rate, installments))


monthly_installment_data()
