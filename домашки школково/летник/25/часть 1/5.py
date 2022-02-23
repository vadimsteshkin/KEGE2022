def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return len(s)
lst=[]
for i in range(231893,251860):
    m=d(i)
    lst.append([m,i])
print(sorted(lst,reverse=True)[0])