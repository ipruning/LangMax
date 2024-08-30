# python 009_fire.py add 10 20

import fire


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def main():
    fire.Fire(
        {
            "add": add,
            "multiply": multiply,
        }
    )


if __name__ == "__main__":
    main()
