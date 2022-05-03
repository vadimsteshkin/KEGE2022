for _ in range(100,1000):
    n=_
    i=0
    while n>0:
        i+=(n%20)
        n//=20
    if i%19==0:
        print(_)
        break