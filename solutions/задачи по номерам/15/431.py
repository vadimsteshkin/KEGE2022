from itertools import *
def f(a1,a2,x):
    p=10<=x<=20
    q=25<=x<=36
    a=a1<=x<=a2
    return (a and not(p))<=q
s=set()
ox=[i/4 for i in range(37*4)]
for a1,a2 in combinations(ox,2):
    if all(f(a1,a2,x) for x in ox):
        s.add(a2-a1)
print(max(s))