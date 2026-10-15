portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}

total_value = 0

print("--- Stock Portfolio ---")

for symbol, stock in portfolio.items():
    stock_value = stock["shares"] * stock["price"]
    total_value += stock_value

    print(f"{symbol}: ${stock_value:.2f}")

print("-----------------------")
print(f"Total Portfolio Value: ${total_value:.2f}")