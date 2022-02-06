def f(n):
    s=set()
    for i in range(2,int(n//2)+1,2):
        if n%i==0:
            s|={i}
            if len(s)>3:
                return [0]
    return s
for i in range(113_000_000,114_000_000):
    k=f(i)
    if len(k)==3:
        print(i,k[-2])