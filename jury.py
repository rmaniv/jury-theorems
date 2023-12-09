from math import comb

def correctness(p, n):
    r = (n // 2) + 1
    P = 0
    while r <= n:
        p_ = (comb(n, r) * (p**r) * ((1 - p)**(n-r)))
        P += p_
        r += 1
    return P
