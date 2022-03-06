for _ in range(10000):
    x=_
    a=0
    b=1
    while x>0:
        if x%2 >0:
            a+=x%8
        else:
            b*=x%8
        x//=8
    if a==2 and b==24:
        print(_)