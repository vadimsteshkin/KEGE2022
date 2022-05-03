for _ in range(1000):
    x=0
    a=0
    b=1
    while x>0:
        a+=1
        b*=(x%10)
        x//=10
    if l==3 and m==0:
        print(_)