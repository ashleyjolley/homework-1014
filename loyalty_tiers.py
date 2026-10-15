customers = {
    "Alice": 750,
    "Bob": 2500,
    "Carol": 6000,
    "David": 1200,
    "Emma": 400
}

tier_counts = {
    "Bronze": 0,
    "Silver": 0,
    "Gold": 0
}

print("--- Customer Loyalty Tiers ---")

for customer, purchases in customers.items():
    if purchases < 1000:
        tier = "Bronze"
    elif purchases < 5000:
        tier = "Silver"
    else:
        tier = "Gold"

    tier_counts[tier] += 1

    print(f"{customer}: {tier}")

print("\n--- Tier Summary ---")

for tier, count in tier_counts.items():
    print(f"{tier}: {count} customers")
