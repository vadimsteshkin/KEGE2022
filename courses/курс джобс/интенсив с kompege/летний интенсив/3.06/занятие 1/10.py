for _ in range(1000):
    s=_
    s=(s-10)//7
    n=1
    while s>0:
        n*=2
        s-=n
    if n==8:
        print(_)
        break