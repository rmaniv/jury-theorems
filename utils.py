import random
from math import ceil, comb
import matplotlib.pyplot as plt
import numpy as np

def majority(n, m=0):
    if m == 0:
        r = (n // 2) + 1
    elif m > 50 and m <= 100: r = ceil((m / 100) * n)
    else:
        print("correctness_simulation(p, n, m) where m = 0 for simple-majority but > 50 and <= 100 for super-majority or unanimity")
        r == None
    return r