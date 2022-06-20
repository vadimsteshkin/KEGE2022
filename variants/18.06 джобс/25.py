def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={n//i,i}
    if len(s)!=0:
        return max(s)+min(s)
    return -1
q=0
for i in range(800000,999999):
    k=f(i)
    if k%138==0:
        print(i,k)
        q+=1
    if q==5:
        break