# P4.py
import numpy as np

def power(v):
    # Calculate power output based on the given equation
    return 5 * v - 3 * (1 - np.log(3.8 - v)) - 1

if __name__ == "__main__":
    v = 2.8
    p = power(v)
    print('power=', p)
