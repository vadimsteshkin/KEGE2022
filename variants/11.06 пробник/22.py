q=0
for _ in range(10**12,10**13):
    x=_
    a=0
    b=0
    while x>0:
        a+=1
        d=x%10
        if d%3==0:
            b+=d
        x//=10
    if a==12 and b==90:
        print(_)
        print(a,b)
        q+=1
print(q)