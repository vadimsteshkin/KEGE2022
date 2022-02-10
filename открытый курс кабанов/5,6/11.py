for _ in range(1,100):
    s=_
    n=1024
    while s>=5:
        s-=5
        n//=2
    if n==64:
        print(_)