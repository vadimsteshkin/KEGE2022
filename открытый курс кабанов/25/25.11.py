def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(300000,99999999):
    m=[x for x in d(i) if x%3==0]
    if len(m)==5:
        print(i,m[4])