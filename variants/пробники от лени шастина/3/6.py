for _ in range(10000):
    s=_
    n=1
    while s<47:
        s+=4
        n*=2
    if n==64:
        print(_)