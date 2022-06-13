for _ in range(100000):
    s=_
    s=(s-10)//7
    n=1
    while s>0:
        n*=2
        s-=n
    if n==1024:print(_)