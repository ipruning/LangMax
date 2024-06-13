import marimo

app = marimo.App(width="medium")


@app.cell
def __():
    1 + 1
    return


@app.cell
def __():
    3 + 3
    return


if __name__ == "__main__":
    app.run()
