from itertools import *
ims=[]
def f(s,e,x):
    b=17<=x<=58
    c=29<=x<=80
    a=s<=x<=e
    return b<=((not(c) and not(a))<=(not(b)))
ox=[i/4 for i in range(81*4)]
for a,b in combinations(ox,2):
    if all(f(a,b,x) for x in ox):
        ims.append(b-a)
print(min(ims))