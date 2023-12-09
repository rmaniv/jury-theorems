from math import ceil, comb

def correctness(p, n, m):
    r = (n // 2) + 1
    P = 0
    while r <= n:
        P += (comb(n, r) * (p**r) * ((1 - p)**(n-r)))
        r += 1
    if n % 2 == 0:
        P += (comb(n, n//2) * (p**(n//2)) * ((1 - p)**(n-(n//2)))) # with coin flip ties
    return P
