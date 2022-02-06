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
for i in range(25317,51238):
    m=[x for x in d(i) if isd(x)]
    if len(m)==6:
        print(i,m)