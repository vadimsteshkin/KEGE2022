def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
           s|={i,n//i}
    return sorted(s)
def kk(p):
    for i in range(len(p)-1):
        if p[i+1]-p[i]!=10:
            return 0
    return 1
for i in range(854321, 1087655):
    m=f(i)
    if len(m)>1:
        if kk(m)==1:
            print(i,min(m))