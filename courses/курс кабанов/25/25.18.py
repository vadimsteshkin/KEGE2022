def d(n):
    s = set()
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            s |= {i, n // i}
    return sorted(s)


for i in range(55_000_000, 60_000_001):
    m = [x for x in d(i) if x % 2 == 1]
    if len(m) == 5:
        print(i, m[-1])
