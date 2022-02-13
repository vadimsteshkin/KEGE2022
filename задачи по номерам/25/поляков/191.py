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
def k(n):
    s=str(d(n))
    if s.count('7')>=4:
        return 1
    else:return 0
q=0
for i in range(10**6,9999999999):
    m=k(i)
    o=d(i)
    if m==1:
        print(i,o)
        q+=1
    if q==5:
        break