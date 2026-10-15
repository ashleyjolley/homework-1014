prices = []

while True:
    price = float(input("Enter item price (0 to finish): $"))

    if price == 0:
        break
    elif price < 0:
        print("Please enter a positive price.")
    else:
        prices.append(price)

total = sum(prices)
number_of_items = len(prices)

print("\n--- Checkout Summary ---")
print(f"Total purchase amount: ${total:.2f}")
print(f"Number of items: {number_of_items}")

if number_of_items > 0:
    average = total / number_of_items
    print(f"Average item cost: ${average:.2f}")
else:
    print("No items were purchased.")
