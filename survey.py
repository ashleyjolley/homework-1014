preferences = ["coffee", "tea", "coffee", "soda"]

counts = {}

for product in preferences:
    if product in counts:
        counts[product] += 1
    else:
        counts[product] = 1

total_responses = len(preferences)

print("--- Market Survey Results ---")

for product, count in counts.items():
    percentage = (count / total_responses) * 100
    print(f"{product.title()}: {percentage:.0f}%")