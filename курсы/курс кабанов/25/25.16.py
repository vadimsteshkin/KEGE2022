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
for i in range(125697,125722):
    m=[x for x in d(i) if isd(x)]
    if len(m)==2 and m[0]*m[1]==i:
        print(m[0],m[1])