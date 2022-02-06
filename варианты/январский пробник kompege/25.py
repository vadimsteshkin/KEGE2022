from functools import *
@lru_cache()
def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return s
for i in range(164700,164753):
    m=sorted(d(i))
    if len(m)==6:
        print(m[-2],m[-1])