import jury

import matplotlib.pyplot as plt
import numpy as np
import random

def condorcet(n_values):
    plt.figure(figsize=(10, 6))
    p_values = np.arange(0, 1.01, 0.01)
    for n in n_values:
        y_values = [jury.correctness(p, n) for p in p_values]
        plt.plot(p_values, y_values, label=f'n={n}', color=np.random.rand(3,))

    plt.title('Probability of Correct Majority Decision by p and N')
    plt.xlabel('Probability of Correctness of Independent Voter (p)')
    plt.ylabel('Probability of Correct Majority Decision')
    plt.legend()
    plt.grid(True)
    plt.show()
