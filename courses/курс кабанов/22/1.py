for _ in range(1,100000000):
    x=_
    a=0
    b=0
    while x>0:
        a+=1
        if x%11>b:
            b=x%11
        x//=11
    if a==7 and b==7:
        print(_)
        break