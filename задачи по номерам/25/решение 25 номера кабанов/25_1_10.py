from functools import *
@lru_cache()
def prime(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return 0
    return 1
@lru_cache()
def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0 and prime(i)==1:
            s.add(i)
    return s
for i in range(25317, 51238):
    m=f(i)
    if len(m)>=6:
        print(i,max(m))