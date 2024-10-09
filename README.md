**scripts**
=====================

A collection of personal scripts for various projects and tasks, including finance and data analysis.

**Contents**
------------

* **Stock Analyzer**: A Python script for retrieving and analyzing stock information, including current price, historical prices, dividends, and financials.
* **Other Scripts**: Additional scripts for various personal projects and tasks.

**Stock Analyzer**
------------------

### Overview

A Python script for retrieving and analyzing stock information, including current price, historical prices, dividends, and financials.

### Features

* Retrieves current stock information, including name, sector, industry, market cap, and beta
* Retrieves historical stock prices, including open, high, low, and close
* Retrieves dividend information, including dividend yield and payout ratio
* Retrieves financial information, including income statement, balance sheet, and cash flow statement
* Formats and displays the retrieved information in a clean and readable format

### Requirements

* Python 3.x
* yfinance library (for retrieving stock information)
* pandas library (for data manipulation and analysis)
* colorama library (for formatting and displaying text)

### Usage

1. Clone this repository to your local machine
2. Navigate to the `stock_analyzer` directory
3. Run the `stock_analyzer.py` script using Python 3.x
4. Enter the stock symbol you want to analyze when prompted
5. The script will retrieve and display the stock information in a clean and readable format

### Example Output

```
Stock Information:
  * Name: Apple Inc.
  * Sector: Technology
  * Industry: Computer Hardware
  * Market Cap: $2.35T
  * Beta: 1.52

Historical Prices:
  * Date        Open   High    Low     Close  Volume
  * 2022-01-01  100.0  105.0   95.0  102.36  45.55M
  * 2022-01-02  102.36 110.0  100.0  108.48  45.56M
  * 2022-01-03  108.48 115.0  105.0  113.04  45.55M

Dividends:
  * Dividend Yield: 0.77%
  * Payout Ratio: 0.22

Financials:
  * Income Statement:
    + Revenue: $274.51B
    + Net Income: $94.68B
    + Earnings Per Share: $10.29
  * Balance Sheet:
    + Cash: $52.53B
    + Debt: $102.61B
    + Equity: $231.46B
  * Cash Flow Statement:
    + Operating Cash Flow: $150.81B
    + Investing Cash Flow: $-127.92B
    + Financing Cash Flow: $-41.39B
```
