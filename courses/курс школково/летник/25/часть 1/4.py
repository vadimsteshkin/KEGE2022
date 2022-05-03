def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    if len(s)==3:
        return 1
    return 0
q=0
for i in range(100100,300301):
    if d(i):
        q+=1
print(q)