from functools import *
@lru_cache()
def prime(n):
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
            return 0
    return 1
def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0 and(prime(i)==1):
           s|={i}
    return s
for i in range(33333,55555):
    m=f(i)
    if len(m)>0:
        if i %sum(m)==0 and sum(m)>250:
            print(i,sum(m))