def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return s
for i in range(1204300,1204381):
    m=sum([x for x in d(i) if x%2==0])
    if m!=0 and m%10==0:
        print(i,m)