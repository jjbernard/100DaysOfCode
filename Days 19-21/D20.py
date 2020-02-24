from itertools import cycle
import sys
import time
import random


def traffic_light(light_rotation):
    for color in light_rotation:
        if color == 'red':
            sys.stdout.write('\r' + 'Red')
            sys.stdout.flush()
            time.sleep(random.randint(2, 4))
        elif color == 'amber':
            sys.stdout.write('\r' + 'Amber')
            sys.stdout.flush()
            time.sleep(1)
        else:
            sys.stdout.write('\r' + 'Green')
            sys.stdout.flush()
            time.sleep(random.randint(3, 6))


if __name__ == '__main__':
    traffic_colors = 'green amber red'.split()
    light_rotation = cycle(traffic_colors)

    traffic_light(light_rotation)
