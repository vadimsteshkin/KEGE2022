from functools import *
@lru_cache()
def F(n, m):
    if m == 0:
        d = 0
    else:
        d = n + F(n, m - 1)
    return d
o=0
for n in range(1,100):
    for m in range(1,100):
        if F(m,n)==30:
            o+=1
            n+=1
print(o)