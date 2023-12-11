from utils import plt, np, ceil, comb, random, majority

def montecarlo(p, n, m):
    trials = int(1e6)
    r = majority(n, m)
    if r is None:
        return None
    return np.sum(np.sum((np.random.random(size=(trials, n)) < p).astype(int), axis=1) >= r) / trials

def deterministic(p, n, m):
    r = majority(n, m)
    if r == None: return None
    P = 0
    while r <= n:
        P += (comb(n, r) * (p**r) * ((1 - p)**(n-r)))
        r += 1
    return P

def plot(n_values, type, m):
    plt.figure(figsize=(10, 6))
    p_values = np.arange(0, 1.01, 0.01)
    for n in n_values:
        y_values = [deterministic(p, n, m) if type == 0 else montecarlo(p, n, m) for p in p_values]
        plt.plot(p_values, y_values, label=f'n={n}', color=np.random.rand(3,))
    plt.title('Probability of Correct Majority Decision by p and n')
    plt.xlabel('Probability of Correctness of Independent Voter (p)')
    plt.ylabel('Probability of Correct Majority Decision')
    plt.legend()
    plt.grid(True)
    plt.show()