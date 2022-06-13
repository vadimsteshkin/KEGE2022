for _ in range(2000):
    x=_
    l=0
    m=0
    while x>0:
        m+=1
        if x%2!=0:
            l+=1
        x//=2
    if l==5 and m==8:
        print(_)
        break