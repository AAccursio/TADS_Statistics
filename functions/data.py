import pandas as pd
import yfinance as yf

def download_history(
    ticker: str,
    multi_level_index: bool = False
) -> pd.DataFrame:
    """
    Plot historical data from Yahoo Finance.

    Args:
        ticker (str): Ticker symbol.
        multi_level_index (bool): Whether to keep the MultiIndex columns.

    """

    df = yf.download(
        tickers=ticker,
        multi_level_index=multi_level_index
    ).reset_index()

    return df