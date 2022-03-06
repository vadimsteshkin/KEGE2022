for _ in range(10000):
    d=_
    n=10
    s=122
    while d!=0 and s//d>0:
        s-=d
        n+=5
    if n==60:
        print(_)