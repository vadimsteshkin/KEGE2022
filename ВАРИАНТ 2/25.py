from functools import *
@lru_cache(None)
def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return s
for i in range(81234,134690):
    m=f(i)
    if len(m)==3:
        print(*m)