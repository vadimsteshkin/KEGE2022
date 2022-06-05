for i in range(1,10000):
    d=i
    n=10
    s=122
    while s//d>0:
        s-=d
        n+=5
    if n==60:
        print(i)
        break