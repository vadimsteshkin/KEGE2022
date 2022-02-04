def d(n):
    s = set()
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            s |= {i, n // i}
    s = sorted(s)
    return s



for i in range(500000000, 999999999999):
    m = d(i)
    if len(m) >= 5:
        o = 1
        for j in range(5):
            o *= m[j]
        if 0 < o<i:
            print(i,m)
