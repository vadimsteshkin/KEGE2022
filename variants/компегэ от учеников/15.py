from itertools import *
def f(x):
    a=30<=x<=50
    p=10<=x<=80
    q=a1<=x<=a2
    return q<=(a and (not(p)))
m=[0]
ox=[i/4 for i in range(10*4,80*4+1)]
for a1,a2 in combinations(ox,2):
    if all(f(x)==1 for x in ox):
        m.append(a2-a1)
        print(min(m))
print(min(m))