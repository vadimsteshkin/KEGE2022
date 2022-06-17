def f(a,b,c,m):
    if a+b>299:return c%2==m%2
    if c==m:return 0
    h=[f(a+3,b,c+1,m),f(a,b+3,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for i in range(1,280):
    for m in range(9):
        if f(20,i,0,m):
            print(i,m)