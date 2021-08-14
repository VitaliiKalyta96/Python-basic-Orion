# 1. Написати програму яка буде обраховувати два квадратних рівняня одночасно,
# всі параметри рівняння задати в змінні.

import logging
import time
import threading
import math


def thread_sqrt_function(name):
    logging.info("Thread %s: start", name)
    time.sleep(2)
    equation_1 = math.sqrt(25)
    equation_2 = math.sqrt(49)
    logging.info(f"Thread {name}: Result equation_1: {equation_1}")
    time.sleep(2)
    logging.info(f"Thread {name}: Result equation_2: {equation_2}")
    time.sleep(2)
    logging.info("Thread %s: finish", name)


structure = "%(asctime)s: %(message)s"
logging.basicConfig(level=logging.INFO, datefmt="%d.%m.%Y %H:%M:%S", format=structure)

action_1 = threading.Thread(target=thread_sqrt_function, args=(1, ))
action_2 = threading.Thread(target=thread_sqrt_function, args=(2, ))
action_1.start()
action_2.start()