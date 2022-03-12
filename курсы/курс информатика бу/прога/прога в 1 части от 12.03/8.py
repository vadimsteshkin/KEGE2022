q=0
for _ in range(10000):
    x=_
    a=0
    b=1
    while x>0:
        a+=1
        if x%14!=0:
            b*=(x%14)
        x//=14
    if a==2 and b==12:
        q+=1
print(q)