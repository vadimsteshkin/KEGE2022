for _ in range(1,100000):
    s=_
    n=1
    while s<94:
        s+=8
        n*=2
    if n==128:
        print(_)
        break