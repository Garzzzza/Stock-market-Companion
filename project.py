import yfinance
import matplotlib.pyplot
import json

portfolio = {}


def main():
    load_portfolio()
    ticker, stock = get_input()
    latest_price, yearly_history = get_stock_history(stock)
    print(f"The latest closing price of {ticker} is ${latest_price:.2f}")
    dividend_yield, dividend_rate = get_dividend(stock)
    print(
        f"Dividend Yield: {dividend_yield*100:.3f}%, Dividend Rate: {dividend_rate:.2f}$"
    )
    plot_and_csv(yearly_history, ticker)

    while True:
        print("\n1. Add to Portfolio")
        print("2. Remove from Portfolio")
        print("3. View Portfolio")
        print("4. Clear Portfolio")
        print("5. Stock research")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_to_portfolio(ticker, latest_price)
        elif choice == "2":
            remove_from_portfolio(ticker, stock)
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            clear_portfolio()
        elif choice == "5":
            main()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def load_portfolio():
    global portfolio
    try:
        with open("portfolio.json", "r") as file:
            portfolio = json.load(file)
        for ticker in portfolio:
            stock = yfinance.Ticker(ticker)
            latest_price, yearly_history = get_stock_history(stock)
            portfolio[ticker] = latest_price
    except FileNotFoundError:
        with open("portfolio.json", "w") as file:
            json.dump({}, file)


def add_to_portfolio(ticker, stock):
    if ticker not in portfolio:
        portfolio[ticker] = stock
        save_portfolio()
        print(f"Added {ticker} to portfolio.")
    else:
        print("This stock is already in the portfolio")


def remove_from_portfolio(ticker, stock):
    if ticker in portfolio:
        del portfolio[ticker]
        save_portfolio()
        print(f"Removed {ticker} from portfolio.")
    else:
        print("Ticker not found in portfolio.")


def view_portfolio():
    if portfolio:
        print("\nPortfolio:")
        for ticker in portfolio:
            latest_price = portfolio[ticker]
            print(f"{ticker}: ${latest_price:.2f}")
    else:
        print("Portfolio is empty.")


def save_portfolio():
    with open("portfolio.json", "w") as file:
        json.dump(portfolio, file, default=str)
    print("Portfolio saved.")


def clear_portfolio():
    global portfolio
    portfolio = {}
    with open("portfolio.json", "w") as file:
        json.dump({}, file)
    print("Portfolio cleared.")


def get_input():
    while True:
        ticker = input("Ticker: ").strip().upper()
        try:
            stock = yfinance.Ticker(ticker)
            if (
                not stock.history(period="1d").empty
                and not stock.history(period="1y").empty
                and stock.info
            ):
                return ticker, stock
            else:
                print(
                    "Here's a list of companies in the stock market and their ticker symbols: https://stockanalysis.com/stocks/"
                )
        except Exception as e:
            print(e)


def get_stock_history(stock):
    try:
        daily_history = stock.history(period="1d")
        if "Close" in daily_history.columns and not daily_history["Close"].empty:
            latest_price = daily_history["Close"].iloc[-1]
            yearly_history = stock.history(period="1y")
        else:
            return
    except Exception as e:
        print(f"Error fetching data: {e}")
        latest_price = None
    return latest_price, yearly_history


def get_dividend(stock):
    try:
        stock_info = stock.info
        dividend_yield = stock_info.get("dividendYield")
        dividend_rate = stock_info.get("dividendRate")
        return dividend_yield, dividend_rate
    except Exception as e:
        print(f"Error fetching data: {e}")


def plot_and_csv(stock_history, ticker):
    stock_history["Close"].plot(title=f"Yearly Trend for {ticker}")
    matplotlib.pyplot.xlabel("Date")
    matplotlib.pyplot.ylabel("Value")
    matplotlib.pyplot.savefig(f"{ticker}_yearly_trend.png")
    stock_history.to_csv(f"{ticker}_yearly_history.csv")
    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()
