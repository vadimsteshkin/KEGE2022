q=0
for _ in range(10000):
    s=_
    n=10
    while s-n<1000:
        s+=n
        n+=5
    if n==80:
        q+=1
        print(_)
print(q)