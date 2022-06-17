def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={n//i,i}
    if len(s)>10:
        k=1
        for i in s:
            k*=i
        if k%2 and sum(s)%2:
            return len(s)
    return 0
q=0
for i in range(800000,1000000000):
    k=f(i)
    if k!=0:
        q+=1
        print(i,k+2)
    if q==6:
        break