a=[]
for  _ in range(0,-100000,-1):
    s=(13+_)*10
    n=512
    while s<0:
        n//=2
        s+=n
    if n==8:
        a.append(_)
        print(_)
print(min(a))