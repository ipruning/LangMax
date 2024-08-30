import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    1 + 1
    return


@app.cell
def __():
    1 + 2
    return


if __name__ == "__main__":
    app.run()
