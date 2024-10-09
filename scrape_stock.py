import yfinance as yf
import pandas as pd
from colorama import init, Fore, Style
init(autoreset=True)

def get_stock_info(symbol):
    """
    Retrieves stock information from Yahoo Finance based on the given symbol.

    Args:
        symbol (str): Stock symbol.

    Returns:
        dict: Stock information.
    """
    ticker = yf.Ticker(symbol)

    stock_info = {
        'symbol': symbol,
        'name': ticker.info.get('shortName'),
        'sector': ticker.info.get('sector'),
        'industry': ticker.info.get('industry'),
        'market_cap': ticker.info.get('marketCap'),
        'current_price': ticker.info.get('currentPrice'),
        'previous_close': ticker.info.get('previousClose'),
        'open_price': ticker.info.get('open'),
        'high_price': ticker.info.get('dayHigh'),
        'low_price': ticker.info.get('dayLow'),
        'volume': ticker.info.get('volume'),
        'averagedailyvolume': ticker.info.get('averageDailyVolume3Month'),
        'fiftytwoweekhigh': ticker.info.get('fiftyTwoWeekHigh'),
        'fiftytwoweeklow': ticker.info.get('fiftyTwoWeekLow'),
        'shares_outstanding': ticker.info.get('sharesOutstanding'),
        'float': ticker.info.get('floatShares'),
        'beta': ticker.info.get('beta'),
        'short_percentage_of_float': ticker.info.get('shortPercentOfFloat')
    }

    return stock_info

def get_historical_prices(symbol, period='1y', interval='1d'):
    """
    Retrieves historical prices of a stock.

    Args:
        symbol (str): Stock symbol.
        period (str): Time period of historical prices (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
        interval (str): Time interval of historical prices (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo').

    Returns:
        pandas DataFrame: Historical prices of the stock.
    """
    ticker = yf.Ticker(symbol)
    historical_prices = ticker.history(period=period, interval=interval)

    return historical_prices


def get_dividends(symbol):
    """
    Retrieves dividend information of a stock.

    Args:
        symbol (str): Stock symbol.

    Returns:
        pandas DataFrame: Dividend information of the stock.
    """
    ticker = yf.Ticker(symbol)
    dividends = ticker.dividends

    return dividends


def get_splits(symbol):
    """
    Retrieves stock split information of a stock.

    Args:
        symbol (str): Stock symbol.

    Returns:
        pandas DataFrame: Stock split information of the stock.
    """
    ticker = yf.Ticker(symbol)
    splits = ticker.splits

    return splits


def get_financials(symbol):
    """
    Retrieves financial information of a stock.

    Args:
        symbol (str): Stock symbol.

    Returns:
        tuple: (Quarterly Income Statement, Quarterly Balance Sheet, Quarterly Cash Flow Statement)
    """
    ticker = yf.Ticker(symbol)
    income_statement = ticker.financials
    balance_sheet = ticker.balance_sheet
    cash_flow_statement = ticker.cashflow

    return income_statement, balance_sheet, cash_flow_statement


def get_analysts(symbol):
    """
    Retrieves analysts' estimates and recommendations of a stock.

    Args:
        symbol (str): Stock symbol.

    Returns:
        tuple: (Analysts' Recommendations, Current Earnings, Dividend Yield, RoA)
    """
    ticker = yf.Ticker(symbol)
    info = ticker.info

    recommendations = {
        "previousSplitFactor": info.get('trailingAnnualDividendRate'),
        "trailingEps": info.get('trailingEps'),
        "lastSplitFactor": info.get('lastSplitFactor'),
        "lastSplitDate": info.get('lastSplitDate')
    }

    current_earnings = {
        "earningsQuarterlyGrowthRate": info.get('earningsQuarterlyGrowthRate')
    }

    dividend_yield = info.get('trailingAnnualDividendRate')

    roa = info.get('returnOnAssets')

    return recommendations, current_earnings, dividend_yield, roa


def format_value(value, unit = ''):
    if isinstance(value, str):
        return value
    elif value is None:
        return 'N/A'
    elif isinstance(value, float) or isinstance(value, int):
        return f"{value:,.2f} {unit}"


def format_currency(value):
    return format_value(value, unit='$')


def format_percent(value):
    return f"{value*100:,.2f}%" if value else "N/A"


def format_bold(s):
    return f"{Style.BRIGHT}{Fore.WHITE}{s}{Style.RESET_ALL}"


def format_green(s):
    return f"{Style.BRIGHT}{Fore.GREEN}{s}{Style.RESET_ALL}"


def format_red(s):
    return f"{Style.BRIGHT}{Fore.RED}{s}{Style.RESET_ALL}"


def format_yellow(s):
    return f"{Fore.YELLOW}{s}{Style.RESET_ALL}"


def main():
    symbol = input(f"{format_bold('Enter a stock symbol (e.g.,AAPL): ')}")
    print("\n")

    print(f"{format_bold('Stock Information:')}")

    stock_info = get_stock_info(symbol)
    for key, value in stock_info.items():
        if key in ['market_cap', 'volume', 'averagedailyvolume']:
            print(f"{format_yellow(key.capitalize())}: {format_currency(value)}")
        elif key in ['current_price', 'previous_close', 'open_price', 'high_price', 'low_price']:
            print(f"{format_yellow(key.capitalize())}: {format_currency(value)}")
        elif key == 'short_percentage_of_float':
            print(f"{format_yellow(key.capitalize())}: {format_percent(value)}")
        elif key in ['shares_outstanding', 'float']:
            print(f"{format_yellow(key.capitalize())}: {format_value(value/1e9, unit='B')}")
        elif key == 'beta':
            print(f"{format_yellow(key.capitalize())}: {format_value(value, unit='x')}")
        else:
            print(f"{format_yellow(key.capitalize())}: {value}")


    print("\n")
    print(f"{format_bold('Historical Prices:')}")

    historical_prices = get_historical_prices(symbol)
    print(historical_prices)

    print("\n")
    print(f"{format_bold('Dividends:')}")

    dividends = get_dividends(symbol)
    print(dividends)

    print("\n")
    print(f"{format_bold('Stock Splits:')}")

    splits = get_splits(symbol)
    print(splits)

    print("\n")
    print(f"{format_bold('Financials:')}")

    income_statement, balance_sheet, cash_flow_statement = get_financials(symbol)
    print(income_statement)
    print(balance_sheet)
    print(cash_flow_statement)

    print("\n")
    print(f"{format_bold('Analysts:')}")

    recommendations, current_earnings, dividend_yield, roa = get_analysts(symbol)

    print("Recommendations:")
    for key, value in recommendations.items():
        print(f"{format_yellow(key.capitalize())}: {value}")

    print("Current Earnings:")
    for key, value in current_earnings.items():
        print(f"{format_yellow(key.capitalize())}: {format_percent(value)}")

    print(f"Dividend Yield: {format_percent(dividend_yield)}")
    print(f"RoA: {format_percent(roa)}")


if __name__ == "__main__":
    main()
