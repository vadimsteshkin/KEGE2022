from itertools import *
def f(s,e,x):
    p=17<=x<=54
    q=37<=x<=83
    a=s<=x<=e
    return p<=((q and (not(a))) <=(not(p)))
ox=[i/4 for i in range(84*4)]
m=[]
for s,e in combinations(ox,2):
    if all(f(s,e,x) for x in ox):
        m.append(e-s)
print(min(m))