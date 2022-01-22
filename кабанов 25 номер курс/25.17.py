from functools import *


@lru_cache(None)
def d(n):
    s = set()
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            s |= {i, n // i}
        if len(s)>3:
            return [False,0]
    if len(s)<3:
        return [False,0]
    return [True,s[-1]]


for i in range(106732567, 152673837):
    m = d(i)
    if m[0]==True:
        print(i, m[1])
