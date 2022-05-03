def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    k=[x for x in s if x%2]
    if len(k)==7:
        return k
    return [0]
for i in range(198374,295382):
    m=d(i)
    if len(m)==7:
        print(sorted(m,reverse=True))