from functools import *
@lru_cache()
def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5)+1)):
        if n%i==0:
            s|={n//i,i}
    return s
lst=[]
for i in range(286564, 287270):
    m=sorted(d(i),reverse=True)

    lst.append([len(m),m[0:2]])
print(*(sorted(lst,reverse=True)[0]))