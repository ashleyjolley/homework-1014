expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}

grand_total = 0

print("--- Expense Summary Report ---")

for category, amounts in expenses.items():
    category_total = 0

    for amount in amounts:
        category_total += amount

    print(f"{category}: ${category_total:.2f}")
    grand_total += category_total

print("------------------------------")
print(f"Grand Total: ${grand_total:.2f}")