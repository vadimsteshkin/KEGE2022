for _ in range(100000000):
    s=_
    s=(s-21)//10
    n=1
    while s>0:
        n*=2
        s-=n
    if n==32:
        print(_)
        break