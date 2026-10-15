revenues = {
    "Year 1": 3,
    "Year 2": 5,
    "Year 3": 8
}

print("--- Projected Revenue Chart ---")

for year, revenue in revenues.items():
    bar = "#" * revenue
    print(f"{year}: {bar}")