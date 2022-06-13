for _ in range(1000000):
    x=_
    a,b=0,0
    while x>0:
        c=x%10
        a+=c
        if b<c:
            b=c
        x//=10
    if a==10 and b==6:
        print(_)
