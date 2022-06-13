from itertools import *
def f(a1,a2,x):
    p=15<=x<=20
    q=5<=x<=38
    a=a1<=x<=a2
    return (a <= p)or q
s=set()
ox=[i/4 for i in range(39*4)]
for a1,a2 in combinations(ox,2):
    if all(f(a1,a2,x) for x in ox):
        s.add(a2-a1)
print(max(s))