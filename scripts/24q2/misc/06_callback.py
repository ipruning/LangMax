from typing import Callable, Optional


def callback(n: int) -> None:
    print(f"Sum = {n}")


def main(a: int, b: int, _callback: Optional[Callable[[int], None]] = None) -> None:
    print(f"adding {a} + {b}")
    if _callback:
        _callback(a + b)


main(1, 3)
main(1, 2, callback)
