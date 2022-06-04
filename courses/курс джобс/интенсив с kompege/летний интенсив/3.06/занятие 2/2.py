for _ in range(1,100000):
    d=_
    c=0
    n=0
    t=d
    while n!=144:
        if n>144:
            c=0
            break
        n+=t
        t+=d
        c+=1
    if c%2:c+=5
    if c==8:print(_)