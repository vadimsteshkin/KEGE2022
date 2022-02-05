def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
            s|={i,n//i}
    s=set(i for i in s if i%2==0)
    return sorted(s)
for i in range(100000, 500001):
    m=f(i)
    if len(m)>150:
        print(i,m[-1]-m[0])