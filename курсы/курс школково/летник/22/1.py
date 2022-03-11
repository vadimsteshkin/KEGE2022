for _ in range(95,9999999999):
    x=_
    l=x
    m=51
    if l%2==0:
        m=36
    while l!=m:
        if l>m:
            l-=m
        else:
            m-=l
    if m==18:
        print(_)
        break