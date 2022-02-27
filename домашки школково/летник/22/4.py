for _ in range(100,9999999999):
    x=_
    l=x-15
    m=x+15
    while l!=m:
        if l>m:
            l-=m
        else:m-=l
    if m==15:
        print(_)
        break