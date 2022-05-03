for _ in range(1,1000):
    x=_
    k=x%6
    a=0
    b=0
    while x>0:
        d=x%6
        if d==k:
            a+=1
        b+=d
        x//=6
    if a==2 and b==15:
        print(_)
        break