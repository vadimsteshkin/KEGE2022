def f(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0:
           s|={i,n//i}
        if len(s)>3:
            return {0,0,0,0}
    return s
for i in range(525784203, 728943762):
    m=f(i)
    if len(m)==3:
        print(i,max(m))