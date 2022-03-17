for _ in range(1000):
    s=_
    n=80
    while s+n<160:
        s+=15
        n-=10
    if s<=100:
        print(_)
        break