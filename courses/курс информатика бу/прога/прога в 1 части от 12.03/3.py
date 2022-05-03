q=0
for _ in range(100000):
    x=_
    s=7*(x//8)
    n=1
    while s<300:
        s+=18
        n*=3
    if n==81:
        q+=1
print(q)