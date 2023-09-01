class Savings:
    #EXCERCISE FOR THE SAVINGS IN PROCESS... THIS MODULE NOT ABOUT THE DELIVERY 2
    def __init__(self, monthly_payment: int, interest: int, estimated_savings: int):
        self.monthly_payment = monthly_payment
        self.interest = interest / 100
        self.estimated_savings = estimated_savings

    def approximate_total_savings_month(self):
        savings_table = []
        accumulated_value = 0

        while accumulated_value < self.estimated_savings:
            interest_payment = round((accumulated_value * self.interest), 2)
            accumulated_value += self.monthly_payment + interest_payment
            print(accumulated_value)
            savings_table.append(accumulated_value)

        print(savings_table)


savings = Savings(9000, 7, 30000)
savings.approximate_total_savings_month()
