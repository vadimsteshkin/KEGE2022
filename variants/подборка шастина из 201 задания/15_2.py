from itertools import *
ims=[]
def f(s,e,x):
    b=18<=x<=52
    c=16<=x<=41
    a=s<=x<=e
    return (b<=a) and (not(c) or a)
ox=[i/4 for i in range(53*4)]
for a,b in combinations(ox,2):
    if all(f(a,b,x) for x in ox):
        ims.append(b-a)
print(min(ims))