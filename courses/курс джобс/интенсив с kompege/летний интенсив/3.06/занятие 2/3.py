for _ in range(1,100000):
    x=_
    a=1
    b=0
    while x>0:
        d=x%10
        a*=d
        if d>5:
            b+=d
        x//=10
        if a==15 and b==120:
            print(_)