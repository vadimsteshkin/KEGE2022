from functools import *
@lru_cache()
def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
            s|={n//i,i}
    if len(s)<3:
        return 0
    s=sorted(s,reverse=True)
    return sum(s[0:2])
@lru_cache()
def f(n):
    k=str(d(n))
    if sorted(k)==list(k) and k!='0':
        return 1
    else:return 0
q=0
for i in range(10**7,210000000000000):
    m=f(i)
    p=d(i)
    if m==1:
        print(i,p)
        q+=1
    if q==5:
        break
