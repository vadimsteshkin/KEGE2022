for _ in range(100):
    x=_
    l=x-15
    m=x+15
    while l!=m:
        if l>m:
            l-=m
        else:m-=l
    if m==15:
        print(_)