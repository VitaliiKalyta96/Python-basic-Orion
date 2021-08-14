# 1. Написати програму яка буде обраховувати два квадратних рівняня одночасно,
# всі параметри рівняння задати в змінні.

import logging
import time
import threading
import math


structure = "%(asctime)s: %(message)s"
logging.basicConfig(level=logging.INFO, datefmt="%d.%m.%Y %H:%M:%S", format=structure)


def thread_sqrt_function(name, a, b, c):
    logging.info("Thread %s: start", name)
    time.sleep(2)
    d = (b ** 2) - (4 * a * c)
    logging.info(f"Thread {name}: numbers: a={a}, b={b}, c={c}")
    y1 = (-b + math.sqrt(d)) / (2 * a)
    y2 = (-b - math.sqrt(d)) / (2 * a)
    logging.info(f"Thread {name}, {d}")
    if d > 0:
        logging.info(f"Thread {name}, y1 = {y1}, y2 = {y2}")
    elif d == 0:
        y = -b / (2 * a)
        logging.info(f"Thread {name}, y = {y}")
    elif d < 0:
        logging.info(f"Not correct value.")
    time.sleep(2)
    logging.info("Thread %s: finish", name)

action_1 = threading.Thread(target=thread_sqrt_function, args=(1, 2, 4, -3))
action_2 = threading.Thread(target=thread_sqrt_function, args=(2, 1, 5, 2))
action_1.start()
action_2.start()
