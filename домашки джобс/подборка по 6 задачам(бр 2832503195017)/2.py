for _ in range(10000):
    d=_
    n=50
    s=101
    while d+n <s:
        s+=50
        n-=10
    if n==50:
        print(_)
