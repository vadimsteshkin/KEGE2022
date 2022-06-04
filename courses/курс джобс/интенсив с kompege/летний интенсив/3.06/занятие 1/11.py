q=0
for _ in range(8,1000008,10):
    d=_
    s=15
    n=10
    while s<=2400:
        s+=d
        n+=5
    if n==50:
        q+=1
print(q)