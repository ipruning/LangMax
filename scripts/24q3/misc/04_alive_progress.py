import time

from alive_progress import alive_bar

for x in 1000, 1500, 700, 0:
    with alive_bar(x) as bar:
        for i in range(1000):
            time.sleep(0.005)
            bar()
