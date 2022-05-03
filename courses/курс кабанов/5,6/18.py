o=0
for _ in range(10,1000):
    s=_
    n=3
    while s*n<243:
        s//=3
        n*=9
    if n==27:
        o+=1
print(o)

