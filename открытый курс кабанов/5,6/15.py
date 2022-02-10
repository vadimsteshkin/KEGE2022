o=0
for _ in range(1,10000):
    d=_
    n=27
    s=12
    while s<=2019:
        s+=d
        n+=16
    if n==171:
        o+=1
print(o)