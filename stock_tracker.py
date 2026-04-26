stock_prices = {"AAPL": 180, "TSLA": 250, "INFY": 20, "GOOGL": 140, "AMZN": 185}
portfolio = {}

try:
    n = int(input("How many stocks do you own? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    n = 0

for i in range(n):
    name = input(f"Stock {i+1} name (e.g. AAPL): ").upper()
    try:
        qty = int(input(f"Quantity of {name}: "))
        portfolio[name] = qty
    except ValueError:
        print("Invalid quantity. Skipping this stock.")

total = 0
print("\n--- Your Portfolio ---")
for stock, qty in portfolio.items():
    if stock in stock_prices:
        value = stock_prices[stock] * qty
        total += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
    else:
        print(f"{stock} not found in our database. Skipping value calculation.")

print(f"\nTotal investment: ${total}")

with open("portfolio.txt", "w") as f:
    f.write("Stock Portfolio Report\n")
    f.write("-" * 25 + "\n")
    for stock, qty in portfolio.items():
        if stock in stock_prices:
            f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
    f.write("-" * 25 + "\n")
    f.write(f"Total Portfolio Value: ${total}\n")

print("Results saved to portfolio.txt")
