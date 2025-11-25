import sys 
import time
import random

def type_out(text, delay=0.02, randomize=False):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if randomize:
            time.sleep(delay + random.uniform(0, delay))
        else:
            time.sleep(delay)
    print()  # New line at the end