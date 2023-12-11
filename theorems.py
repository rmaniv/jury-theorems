from utils import plt, np
import jury

def condorcet(n_values, type, m):
    plt.figure(figsize=(10, 6))
    p_values = np.arange(0, 1.01, 0.01)
    for n in n_values:
        y_values = [jury.deterministic(p, n, m) if type == 0 else jury.montecarlo(p, n, m) for p in p_values]
        plt.plot(p_values, y_values, label=f'n={n}', color=np.random.rand(3,))
    plt.title('Probability of Correct Majority Decision by p and n')
    plt.xlabel('Probability of Correctness of Independent Voter (p)')
    plt.ylabel('Probability of Correct Majority Decision')
    plt.legend()
    plt.grid(True)
    plt.show()
