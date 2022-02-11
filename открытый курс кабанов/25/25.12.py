def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(550000,10000000):
    k = [x for x in d(i) if x%10==7]
    if len(k)==3:
        print(i,k[-1])