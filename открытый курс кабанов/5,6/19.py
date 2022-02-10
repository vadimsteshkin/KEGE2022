o=0
for i in range(1,100000):
    d=i
    n=20
    s=40
    while s+n<d:
        s-=10
        n-=20
    o+=1
print(o)