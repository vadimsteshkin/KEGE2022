for _ in range(10000):
    s=_
    s//=100
    n=1
    while s<51:
        s+=5
        n*=2
    if n==128:print(_)