from itertools import *
def f(a1,a2,x):
    a=a1<=x<=a2
    p=5<=x<=20
    q=25<=x<=38
    return (a<=p) or q
ox=[i/4 for i in range(39*4)]
ans=set()
for a1,a2 in combinations(ox,2):
    if all(f(a1,a2,x) for x in ox):
        ans.add(a2-a1)
print(max(ans))