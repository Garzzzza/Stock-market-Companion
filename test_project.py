import pytest
import project
import yfinance
from unittest.mock import patch
import os


def test_get_input_valid():
    with patch("builtins.input", return_value="AAPL"):
        ticker, stock = project.get_input()
        assert ticker == "AAPL"
        assert isinstance(stock, yfinance.Ticker)
        assert not stock.history(period="1d").empty
        assert stock.info is not None


def test_get_stock_history():
    stock = yfinance.Ticker("NVDA")
    latest_price, yearly_history = project.get_stock_history(stock)
    daily_history = stock.history(period="1d")
    assert not daily_history.empty
    assert not yearly_history.empty
    assert not latest_price is None


def test_get_dividend():
    stock = yfinance.Ticker("NVDA")
    stock_info = stock.info
    assert not stock_info.get("dividendYield") is None
    assert not stock_info.get("dividendRate") is None


def test_plot_and_csv():
    ticker = "NVDA"
    stock = yfinance.Ticker(ticker)
    yearly_history = stock.history(period="1y")
    project.plot_and_csv(yearly_history, ticker)
    assert os.path.exists(f"{ticker}_yearly_trend.png")
    assert os.path.exists(f"{ticker}_yearly_history.csv")
    os.remove(f"{ticker}_yearly_trend.png")
    os.remove(f"{ticker}_yearly_history.csv")
