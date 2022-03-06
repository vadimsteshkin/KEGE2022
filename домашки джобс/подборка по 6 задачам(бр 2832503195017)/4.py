for _ in range(1000):
    d=_
    n=2
    s=0
    while s<=365:
        s+=d
        n+=5
    if n==67:
        print(_)