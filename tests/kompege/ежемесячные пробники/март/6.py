q=0
for _ in range(1000):
    s=_
    s//=15
    n=14
    while s<285:
        if (s+n)%9==0:
            s+=11
        n+=13
    if n==118:
        q+=1
        print(q)