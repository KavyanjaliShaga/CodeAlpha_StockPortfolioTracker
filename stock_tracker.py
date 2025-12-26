# Stock Portfolio Tracker

stock_prices = {
    "SPRITE": 180,
    "MAAZA": 250,
    "THUMBSUP": 140,
    "STING": 130
}

total_value = 0
portfolio = []

print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_value += value
        portfolio.append(f"{stock} - Qty: {quantity}, Value: ${value}")
    else:
        print("Stock not found!")

print("\nYour Portfolio:")
for item in portfolio:
    print(item)

print(f"\nTotal Investment Value: ${total_value}")

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for item in portfolio:
        file.write(item + "\n")
    file.write(f"\nTotal Investment Value: ${total_value}")

print("\nPortfolio saved to portfolio.txt")