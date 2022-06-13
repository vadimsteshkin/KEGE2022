from itertools import *
f=[str(i)*k for i in range(9999) for k in range(6)]
k=sorted(set(f))
a=[]
for i in k:
    m=int('12'+i+'6789')
    if m<10**8 and m%39==0:
        a.append([m,m//39])
a=sorted(a)
for i in a:
    print(*i)