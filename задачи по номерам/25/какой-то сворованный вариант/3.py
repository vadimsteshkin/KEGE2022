def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
           s|={i,n//i}
    return s
for i in range(321653, 654322,2):
    s=f(i)
    ch=[x for x in s if x%2==0]
    if len(ch)==0 and len(s)>70:
        print(i,max(s))