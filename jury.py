from math import ceil, comb

def correctness(p, n, m):
    # simple majority
    if m == 0:
        r = (n // 2) + 1
    # super majority or unanimity (for ex, m should be 75 if prefered super-majority level is 75%)
    elif m > 50 and m <= 100:
        r = ceil((m/100) * n)
    else:
        print("correctness(p, n, m) where m = 0 for simple-majority but > 50 and <= 100 for super-majority or unanimity")
        return None
    P = 0
    while r <= n:
        P += (comb(n, r) * (p**r) * ((1 - p)**(n-r)))
        r += 1
    return P
