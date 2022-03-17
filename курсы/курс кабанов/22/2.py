for _ in range(1,100000000):
    x=_
    a=2
    b=3
    while x>0:
        d=x%4
        a*=d
        if d<3:
            b+=d
        x//=4
    if a==24 and b==16:
        print(_)