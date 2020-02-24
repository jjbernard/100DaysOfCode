from itertools import cycle
import sys
import time
import random

if __name__ == '__main__':
    traffic_colors = 'green amber red'.split()

    traffic_light = cycle(traffic_colors)

    while True:
        sys.stdout.write('\r' + next(traffic_light))
        sys.stdout.flush()
        time.sleep(random.randint(1, 4))
