for _ in range(10000):
    a=_
    r=9
    l=0
    while a>=r:
        l+=1
        a-=r
    m=a
    if m<l:
        m=l
        l=a
    if l==2 and m==8:
        print(_)
        break