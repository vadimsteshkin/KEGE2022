def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(412500,412671):
    k=d(i)
    if len(k)==6:
        print(i, *k) 