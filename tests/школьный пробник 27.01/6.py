for m in range(10000):
    s=m
    n = 105
    while n > s:
        s = s + 3
        n=n-2
    if n==67:
        print(m)