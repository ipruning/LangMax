import time

from joblib import Memory

location = "./cache"
memory = Memory(location, verbose=0)


@memory.cache
def my_function(x, y):
    time.sleep(1)
    return x + y


print(my_function(1, 2))
print(my_function(1, 2))
