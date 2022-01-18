from functools import *


@lru_cache(None)
def d(n):
    s = set()
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            s |= {i, n // i}
    return sorted(s)


for i in range(106732567, 152673837):
    m = d(i)
    if len(m) == 3:
        print(i, m[-1])
