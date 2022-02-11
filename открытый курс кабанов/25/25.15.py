def isd(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(500000,2,-1):
    m=sum([x for x in d(i) if isd(x)])
    if m%10==0 and m!=0:
        print(i,m)