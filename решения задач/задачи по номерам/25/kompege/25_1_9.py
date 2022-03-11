from functools import *
_=[49,25,169]
@lru_cache()
def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)

for i in range(224466, 664422):
    m=f(i)
    if len(m)>0:
        if max(m)<100000 and i%(13*5*7)==0 and ((49 not in m) and (25 not in m) and (169 not in m)) and max(m)%100==19:
            print(i , max(m))