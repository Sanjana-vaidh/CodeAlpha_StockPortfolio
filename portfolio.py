import csv


def calculate_portfolio():
    # Hardcoded stock prices as specified in the instructions
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 410,
        "AMZN": 175,
    }

    portfolio = []
    total_investment = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks in database:", ", ".join(stock_prices.keys()))

    while True:
        symbol = (
            input("\nEnter stock ticker (or type 'done' to finish): ")
            .strip()
            .upper()
        )

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print("Stock not found in price database. Please try again.")
            continue

        try:
            quantity = int(
                input(f"Enter quantity of shares for {symbol}: ").strip()
            )
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
            continue

        price = stock_prices[symbol]
        investment_value = price * quantity
        total_investment += investment_value

        portfolio.append(
            {
                "symbol": symbol,
                "quantity": quantity,
                "price": price,
                "value": investment_value,
            }
        )

        print(
            f"Added {quantity} shares of {symbol} at ${price} each (Total: ${investment_value})."
        )

    # Display portfolio summary
    print("\n" + "=" * 35)
    print("PORTFOLIO SUMMARY")
    print("=" * 35)

    if not portfolio:
        print("No stocks added to portfolio.")
        return

    for item in portfolio:
        print(
            f"{item['symbol']}: {item['quantity']} shares @ ${item['price']} = ${item['value']}"
        )

    print("-" * 35)
    print(f"Total Investment Value: ${total_investment}")
    print("=" * 35)

    # Optional file export
    save_option = (
        input("\nWould you like to save this result to a file? (yes/no): ")
        .strip()
        .lower()
    )

    if save_option in ["yes", "y"]:
        filename = "portfolio_summary.csv"
        try:
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Stock Symbol", "Quantity", "Price Per Share ($)", "Total Value ($)"]
                )
                for item in portfolio:
                    writer.writerow(
                        [
                            item["symbol"],
                            item["quantity"],
                            item["price"],
                            item["value"],
                        ]
                    )
                writer.writerow([])
                writer.writerow(
                    ["Total Portfolio Value", "", "", total_investment]
                )

            print(f"Success! Portfolio saved to {filename}")
        except IOError:
            print("An error occurred while writing to the file.")


if __name__ == "__main__":
    calculate_portfolio()