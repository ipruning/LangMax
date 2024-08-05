import time

import numpy as np


def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
        return result

    return wrapper


def basel(N: int) -> float:
    return sum(x ** (-2) for x in range(1, N))


def basel_less_pythonic(N: int) -> float:
    s = 0.0
    for x in range(1, N):
        s += x ** (-2)
    return s


def basel_np(N: int) -> float:
    # [1, 1, ..., 1]
    ones = np.ones(N - 1)
    # [1, 2, ..., N]
    r = np.arange(1, N)
    # [1, 1/2, ..., 1/N]
    div = ones / r
    # [1, 1/4, ..., 1/N^2]
    inv_squares = np.square(div)
    # ~ pi^2/6
    return float(np.sum(inv_squares))


f_1 = time_function(basel)
f_2 = time_function(basel_less_pythonic)
f_3 = time_function(basel_np)
f_3(100000000)
