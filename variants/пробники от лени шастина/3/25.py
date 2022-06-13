def p(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={n//i,i}
    s=sorted(s)
    if len(s)>1:
        return max(s)+min(s)
    return 0
q=0
for i in range(220000,9999999):
    k=p(i)
    if k%10==4:
        print(i,k)
        q+=1
    if q==5:break