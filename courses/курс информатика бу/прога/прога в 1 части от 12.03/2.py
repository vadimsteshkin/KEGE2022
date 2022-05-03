for _ in range(1000):
    s=_
    n=0
    while s<s**2:
        s-=1
        n+=3
    if n>2000:
        print(_)
        break