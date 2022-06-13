for _ in range(1,10000):
    d=_
    n=3
    s=57
    while s<=1200:
        s+=d
        n+=4
    if n==63:
        print(_)
        break
