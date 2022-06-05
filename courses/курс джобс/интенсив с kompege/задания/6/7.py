for _ in range(10000):
    n=0
    s=_
    while s**2<101:
        s+=1
        n+=2
    if n==16:
        print(_)