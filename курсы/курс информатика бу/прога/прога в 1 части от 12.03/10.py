for _ in range(100,10000):
    x=_
    l=x-21
    m=x+12
    while l!=m:
        if l>m:
            l-=m
        else:m-=l
    if m==11:
        print(_)
        break