import random
from time import sleep

def human_sleep(min_s=3.0, max_s=8.0):
    sleep(random.uniform(min_s, max_s))