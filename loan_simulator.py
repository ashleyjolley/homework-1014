def calculate_repayment(loan_amount, annual_rate, monthly_payment):
    balance = loan_amount
    monthly_rate = annual_rate / 100 / 12
    months = 0

    while balance > 0:
        interest = balance * monthly_rate

        if monthly_payment <= interest:
            print("The monthly payment is too low to repay this loan.")
            return

        balance += interest
        balance -= monthly_payment
        months += 1

        if balance < 0:
            balance = 0

    print(f"Loan paid off in {months} months.")

loan_amount = float(input("Enter loan amount: $"))
annual_rate = float(input("Enter annual interest rate (%): "))
monthly_payment = float(input("Enter monthly payment: $"))

if loan_amount <= 0:
    print("Loan amount must be greater than zero.")
elif annual_rate < 0:
    print("Interest rate cannot be negative.")
elif monthly_payment <= 0:
    print("Monthly payment must be greater than zero.")
else:
    calculate_repayment(
        loan_amount,
        annual_rate,
        monthly_payment
    )
