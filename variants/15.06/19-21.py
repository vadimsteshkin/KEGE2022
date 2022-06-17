def f(a,b,c,m):
    if a+b>230:return c%2==m%2
    if c==m:return 0
    h=[f(a,b+2,c+1,m),f(a+2,b,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if c%2!=m%2 else any(h)
for a in range(214):
    for m in range(6):
        if f(17,a,0,m):
            print(a,m)
            break