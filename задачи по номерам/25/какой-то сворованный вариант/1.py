def f(n):
    s=set()
    for i in range(1,int(pow(n,0.5)+1)):
        if n%i==0:
            k=abs(n//i-i)
    return s
for i in range(2*10**6,3*10**6):
    m=f(i)
    if len(m)>2 and max(m)<120:
        print(i)
