import plotly.express as px
from plotly.graph_objects import Figure
from functions.data import download_history

def plot_history(ticker:str) -> Figure:
    """
    Download historical data from Yahoo Finance.

    Args:
        ticker (str): Ticker symbol.
        multi_level_index (bool): Whether to keep the MultiIndex columns.

    Returns:
        pd.DataFrame: Historical price data.
    """

    df = download_history(ticker)
    
    fig = px.line(
        df,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} stock price.'
    )
    
    return fig