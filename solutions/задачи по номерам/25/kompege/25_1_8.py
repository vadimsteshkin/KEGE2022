from functools import *
@lru_cache()
def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
            s|={i,n//i}
    return s
for i in range(321654, 654321):
    m=f(i)
    if all(x%2==1 for x in m) and len(m)>70:
        print(i,max(m))
