---
layout: page
title: 🎯 Common Trading Strategies
---

# 🎯 Common Trading Strategies

<!-- **Week 5 (Days 31-37): Common Trading Strategies & Python Data Handling** -->

*   **Day 31: Swing Trading Strategies**
    *   **Topic:** Capturing shorter-term market moves (a few days to a few weeks).
    *   **Key Concepts:** Identifying swings within a larger trend. Using technical indicators for entry/exit (e.g., MAs, RSI, Stochastics, support/resistance bounces). Typical holding periods. Risk management for swing trades.
    *   **Hands-on Activity:** Research 2-3 common swing trading setups (e.g., pullback to a moving average, RSI divergence confirmation). Back-test one setup manually on historical charts for 2 stocks over the past 6 months. Record hypothetical trades in your journal.
    *   **Recommended Resources:**
        *   Investopedia - Swing Trading: [https://www.investopedia.com/terms/s/swingtrading.asp](https://www.investopedia.com/terms/s/swingtrading.asp)
        *   Book: "Mastering the Swing Trade" by Alan S. Farley.
        *   YouTube channels focusing on swing trading strategies.

*   **Day 32: Trend Following Strategies**
    *   **Topic:** Strategies designed to profit from sustained directional market movements.
    *   **Key Concepts:** Identifying strong trends (e.g., using ADX, longer-term MAs). Entry signals (e.g., breakout from consolidation, MA crossover). Trailing stop-loss techniques to ride the trend. Challenges (whipsaws in ranging markets).
    *   **Hands-on Activity:** Identify 2 stocks that have been in strong uptrends or downtrends recently. Apply a simple trend following strategy (e.g., enter on a 20/50 EMA crossover, use a 20-period ATR trailing stop) on their historical charts. Note how long the trend lasted and how the strategy performed.
    *   **Recommended Resources:**
        *   Investopedia - Trend Trading: [https://www.investopedia.com/terms/t/trendtrading.asp](https://www.investopedia.com/terms/t/trendtrading.asp)
        *   Book: "Trend Following" by Michael Covel.

*   **Day 33: Breakout Trading Strategies**
    *   **Topic:** Trading the price movement that occurs when a stock breaks out of a defined range or pattern.
    *   **Key Concepts:** Identifying key support/resistance levels or chart patterns (triangles, flags, ranges). Volume confirmation on breakouts. Managing false breakouts. Setting profit targets and stop-losses for breakout trades.
    *   **Hands-on Activity:** Look for 5 examples of breakouts from consolidation patterns (e.g., rectangles, triangles) on historical charts. Note the volume on the breakout day and the subsequent price movement. Paper trade a breakout strategy.
    *   **Recommended Resources:**
        *   Investopedia - Breakout: [https://www.investopedia.com/terms/b/breakout.asp](https://www.investopedia.com/terms/b/breakout.asp)
        *   BabyPips - Breakout Trading (forex focused, but concepts apply): [https://www.babypips.com/learn/forex/breakout-trading](https://www.babypips.com/learn/forex/breakout-trading)

*   **Day 34: Range Trading (Mean Reversion) Strategies**
    *   **Topic:** Profiting from price oscillations within a defined trading range.
    *   **Key Concepts:** Identifying well-defined support and resistance levels that form a trading range. Using oscillators (RSI, Stochastics) to identify overbought conditions near resistance and oversold conditions near support. Setting profit targets within the range and stop-losses outside the range.
    *   **Hands-on Activity:** Find 2 stocks that appear to be trading in a range. Apply RSI or Stochastics. Paper trade entries when the oscillator is oversold near support and exits near resistance (or vice-versa for short trades).
    *   **Recommended Resources:**
        *   Investopedia - Range Trading: [https://www.investopedia.com/terms/r/rangeboundtrading.asp](https://www.investopedia.com/terms/r/rangeboundtrading.asp)
        *   Investopedia - Mean Reversion: [https://www.investopedia.com/terms/m/meanreversion.asp](https://www.investopedia.com/terms/m/meanreversion.asp)

*   **Day 35: Python for Data Acquisition: yfinance & pandas-datareader**
    *   **Topic:** Using Python to download historical stock price data.
    *   **Key Concepts:** `yfinance` library for accessing Yahoo Finance data. `pandas-datareader` for accessing various data sources (though Yahoo Finance via this can be less reliable than `yfinance` directly). Fetching OHLCV (Open, High, Low, Close, Volume) data. Adjusting for stock splits and dividends.
    *   **Hands-on Activity:** Write a Python script using `yfinance` to download 5 years of daily historical data for 3 different stocks. Save each dataset to a CSV file. Load one of the CSV files back into a Pandas DataFrame and display the first 5 rows.
    *   **Recommended Resources:**
        *   `yfinance` PyPI page: [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)
        *   `pandas-datareader` Documentation: [https://pandas-datareader.readthedocs.io/en/latest/](https://pandas-datareader.readthedocs.io/en/latest/)
        *   Tutorials on YouTube for "yfinance tutorial".

*   **Day 36: Data Cleaning & Preparation with Pandas**
    *   **Topic:** Ensuring your financial data is accurate and ready for analysis.
    *   **Key Concepts:** Handling missing data (NaN values) - identifying and deciding how to treat them (e.g., fill forward, backward fill, drop). Checking for outliers or erroneous data. Converting data types (e.g., date strings to datetime objects). Setting a DatetimeIndex.
    *   **Hands-on Activity:** Using the stock data downloaded on Day 35, check for any missing values in your DataFrames. Practice different methods of handling them (e.g., `fillna()`, `dropna()`). Ensure the \'Date\' column is a DatetimeIndex.
    *   **Recommended Resources:**
        *   Pandas Documentation - Working with missing data: [https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)
        *   Real Python - Pandas Data Cleaning: [https://realpython.com/python-pandas-tricks/](https://realpython.com/python-pandas-tricks/) (search for cleaning sections)

*   **Day 37: Review of Week 5 & Strategy/Python Practice**
    *   **Topic:** Consolidating knowledge of common strategies and basic data handling in Python.
    *   **Key Concepts:** Review swing, trend, breakout, and range trading. Review Python data acquisition and cleaning.
    *   **Hands-on Activity:** Choose one trading strategy from the week. Write down its rules very clearly. Then, using Python and the data you downloaded/cleaned, try to identify historical instances where the entry conditions for this strategy might have occurred. (No backtesting yet, just data exploration). Continue paper trading, focusing on one or two strategies from the week.



