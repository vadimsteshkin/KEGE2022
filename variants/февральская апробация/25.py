from  functools import *
@lru_cache()
def m(s):
    a=set()
    for i in range(2,int(pow(s,0.5)+1)):
        if s%i==0:
            a|={i,s//i}
    if len(a)>0:
        return max(a)+min(a)
    return 0
q=0
for i in range(220001,9999999999999):
    k=m(i)
    if k%10==4:
        print(i,k)
        q+=1
    if q==5:
        break