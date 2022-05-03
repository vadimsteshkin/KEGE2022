def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    if len(s)==3:
        return True
    return False
for i in range(300000,333000):
    if d(i):
        print(i)