def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    k=[x for x in s if x%3==0]
    if len(s)-len(k)!=0:
        o=len(k)/(len(s)-len(k))
    else:o=0
    if o>2:
        return [1,len(k)-len(s)]
    else:return [0]
for i in range(100500,100701):
    m=d(i)
    if len(m)>1:
        print(i,m[1])
