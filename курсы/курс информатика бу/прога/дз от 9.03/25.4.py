def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(111111,123124):
    k=d(i)
    if len(k)==2:
        print(i,*k)