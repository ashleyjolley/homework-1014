sales = {
    "Alice": 5000,
    "Bob": 7000,
    "Carol": 3000
}

def calculate_commission(sales_amount):
    return sales_amount * 0.10

commissions = {}

for employee, amount in sales.items():
    commission = calculate_commission(amount)
    commissions[employee] = commission

leaderboard = sorted(
    commissions.items(),
    key=lambda employee: employee[1],
    reverse=True
)

print("--- Commission Leaderboard ---")

for employee, commission in leaderboard:
    print(f"{employee}: ${commission:.2f}")
