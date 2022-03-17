q=0
for _ in range(1,100000000):
    x=_
    a=0
    b=0
    while x>0:
        a+=1
        if x%2!=0:
            b+=1
        x//=2
    if a==16 and b==14:
        q+=1
        print(q)