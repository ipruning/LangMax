import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium", app_title="Great Tables")


@app.cell
def __():  # type: ignore
    from great_tables import GT, html
    from great_tables.data import sp500, sza

    return GT, html, sp500, sza


@app.cell
def __(GT, sp500):  # type: ignore
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
    return end_date, sp500_mini, start_date


@app.cell
def __(GT, html, sza):
    import polars as pl
    import polars.selectors as cs

    sza_pivot = (
        pl.from_pandas(sza)
        .filter((pl.col("latitude") == "20") & (pl.col("tst") <= "1200"))
        .select(pl.col("*").exclude("latitude"))
        .drop_nulls()
        .pivot(values="sza", index="month", columns="tst", sort_columns=True)
    )

    (
        GT(sza_pivot, rowname_col="month")
        .data_color(
            domain=[90, 0],
            palette=["rebeccapurple", "white", "orange"],
            na_color="white",
        )
        .tab_header(
            title="Solar Zenith Angles from 05:30 to 12:00",
            subtitle=html("Average monthly values at latitude of 20&deg;N."),
        )
        .sub_missing(missing_text="")
    )
    return cs, pl, sza_pivot


if __name__ == "__main__":
    app.run()
