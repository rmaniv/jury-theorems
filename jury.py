from math import ceil, comb
import random

def correctness(p, n, m, num_trials=int(1e6)):
    if m == 0:
        if n % 2:
            required_majority = (n // 2) + 1
        else:
            required_majority = n // 2
    elif 50 < m <= 100:
        required_majority = ceil((m / 100) * n)
    else:
        print("correctness_simulation(p, n, m) where m = 0 for simple-majority but > 50 and <= 100 for super-majority or unanimity")
        return None

    successful_trials = 0
    for _ in range(num_trials):
        votes = sum(random.random() < p for _ in range(n))
        if votes >= required_majority:
            successful_trials += 1

    return successful_trials / num_trials