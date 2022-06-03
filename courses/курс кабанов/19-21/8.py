def f(a,c,m):
    if a>=2163:return c%2==m%2
    if c==m:return 0
    h=[f(a+1,c+1,m),f(a*3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for a in range(2000,200,-1):
    for m in range(1,10):
        if f(a,0,m):
            print(a,m)
            break

