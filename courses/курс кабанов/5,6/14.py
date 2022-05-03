for _ in range(1,10000):
    s=_
    n=1
    while s<=45:
        s+=4
        n*=2
    if n==256:
        print(_)