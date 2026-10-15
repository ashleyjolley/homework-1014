warehouses = [
    {
        "name": "Warehouse A",
        "inventory": {"apples": 100, "bananas": 150}
    },
    {
        "name": "Warehouse B",
        "inventory": {"apples": 200, "bananas": 100}
    }
]

totals = {}

for warehouse in warehouses:
    print(f"Checking {warehouse['name']}")

    for product, quantity in warehouse["inventory"].items():
        if product in totals:
            totals[product] += quantity
        else:
            totals[product] = quantity

print("\n--- Total Supply Chain Inventory ---")

for product, quantity in totals.items():
    print(f"{product.title()}: {quantity}")
