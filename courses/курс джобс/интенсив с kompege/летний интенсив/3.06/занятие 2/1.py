for _ in range(10000):
    x=_
    q=7
    p=10
    k1=0
    k2=0
    while x<=100:
        k1+=1
        x+=p
    while x>=q:
        k2+=1
        x-=q
    l=x+k1
    m=x+k2
    if l==11 and m==20:
        print(_)