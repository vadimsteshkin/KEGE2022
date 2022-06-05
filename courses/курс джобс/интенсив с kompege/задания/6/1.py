for _ in range(100000):
    s=_
    n=1
    while s<=70:
        s+=9
        n*=7
    if n==343:
        print(_)
        break