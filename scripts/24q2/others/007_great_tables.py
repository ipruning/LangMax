import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium", app_title="Great Tables")


@app.cell
def __():
    from great_tables import GT
    from great_tables.data import sp500

    # Define the start and end dates for the data range
    start_date = "2010-06-07"
    end_date = "2010-06-14"

    # Filter sp500 using Pandas to dates between `start_date` and `end_date`
    sp500_mini = sp500[(sp500["date"] >= start_date) & (sp500["date"] <= end_date)]

    # Create a display table based on the `sp500_mini` table data
    (
        GT(sp500_mini)
        .tab_header(title="S&P 500", subtitle=f"{start_date} to {end_date}")
        .fmt_currency(columns=["open", "high", "low", "close"])
        .fmt_date(columns="date", date_style="wd_m_day_year")
        .fmt_number(columns="volume", compact=True)
        .cols_hide(columns="adj_close")
    )
    return GT, end_date, sp500, sp500_mini, start_date


@app.cell
def __(GT):
    import pandas as pd
    import numpy as np

    # Generate fake data for YGO card trading
    np.random.seed(0)
    _dates = pd.date_range(start="2023-01-01", periods=10, freq='D')
    _card_names = [f"Card_{i}" for i in range(1, 11)]
    _open_prices = np.random.uniform(1, 100, size=10)
    _high_prices = _open_prices + np.random.uniform(1, 10, size=10)
    _low_prices = _open_prices - np.random.uniform(1, 10, size=10)
    _close_prices = np.random.uniform(1, 100, size=10)
    _volumes = np.random.randint(100, 1000, size=10)

    _ygo_data = pd.DataFrame({
        "date": _dates,
        "card_name": _card_names,
        "open": _open_prices,
        "high": _high_prices,
        "low": _low_prices,
        "close": _close_prices,
        "volume": _volumes
    })

    # Define the start and end dates for the data range
    _start_date = "2023-01-01"
    _end_date = "2023-01-10"

    # Filter _ygo_data using Pandas to dates between `_start_date` and `_end_date`
    _ygo_mini = _ygo_data[(_ygo_data["date"] >= _start_date) & (_ygo_data["date"] <= _end_date)]

    # Create a display table based on the `_ygo_mini` table data
    (
        GT(_ygo_mini)
        .tab_header(title="YGO Card Trading", subtitle=f"{_start_date} to {_end_date}")
        .fmt_currency(columns=["open", "high", "low", "close"])
        .fmt_date(columns="date", date_style="wd_m_day_year")
        .fmt_number(columns="volume", compact=True)
    )
    return np, pd


if __name__ == "__main__":
    app.run()
