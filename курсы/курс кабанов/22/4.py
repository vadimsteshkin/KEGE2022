q=0
for _ in range(1,10000):
    for y1 in range(1,10000):
        x=_
        y=y1
        a=0
        b=0
        while x*y>0:
            if x>0:
                a+=1
            if y>0 and y%7>b:
                b=y%7
            x//=10
            y//=7
    if a==4 and b==5:
        q=max(q,_*y1)
        print(q)