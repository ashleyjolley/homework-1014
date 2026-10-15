revenue = float(input("Enter initial annual revenue: $"))
growth_rate = float(input("Enter annual growth rate (%): "))

print("\n--- Revenue Growth Projection ---")
print(f"{'Year':<10}{'Projected Revenue':>20}")

for year in range(1, 11):
    revenue = revenue * (1 + growth_rate / 100)
    print(f"{year:<10}${revenue:,.2f}")