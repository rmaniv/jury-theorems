from utils import ceil, comb, random

def majority(n, m):
    if m == 0:
        if n % 2:
            r = (n // 2) + 1
        else:
            r = n // 2
    elif 50 < m <= 100:
        r = ceil((m / 100) * n)
    else:
        print("correctness_simulation(p, n, m) where m = 0 for simple-majority but > 50 and <= 100 for super-majority or unanimity")
        r == None
    return r

def montecarlo(p, n, m, trials=int(1e6)):
    r = majority(n, m)
    if r == None:
        return None
    successful = 0
    for _ in range(trials):
        votes = sum(random.random() < p for _ in range(n))
        if votes >= r:
            successful += 1
    return successful / trials

def deterministic(p, n, m):
    r = majority(n, m)
    if r == None:
        return None
    r = (n // 2) + 1
    P = 0
    while r <= n:
        P += (comb(n, r) * (p**r) * ((1 - p)**(n-r)))
        r += 1
    if n % 2 == 0:
        P += (comb(n, n//2) * (p**(n//2)) * ((1 - p)**(n-(n//2)))) # with coin flip ties
    return P