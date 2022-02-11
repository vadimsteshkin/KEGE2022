def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(6080068,6080177):
    if len(d(i))==0:
        print(i)