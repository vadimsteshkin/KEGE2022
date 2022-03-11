def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(500000,9999999):
    m=[x for x in d(i) if x%10==8 and x!=8]
    if len(m)>0:
        print(i,m[0])