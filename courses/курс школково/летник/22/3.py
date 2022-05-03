for _ in range(100,9999999999):
    x=_
    l=2*x-40
    m=2*x+40
    while l!=m:
        if l>m:
            l-=m
        else:m-=l
    if m==40:
        print(_)
        break