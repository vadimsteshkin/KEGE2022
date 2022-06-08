for _ in range(100000):
    x=_
    a=0
    b=1
    while x>0:
        a+=1
        b*=x%10
        x//=10
    if a==2 and b==14:
        print(_)