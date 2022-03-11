for _ in range(100,9999999999):
    x=_
    l=x-20
    m=x+20
    while l!=m:
        if l>m:
            l-=m
        else:
            m-=l
    if m==20:
        print(_)
        break