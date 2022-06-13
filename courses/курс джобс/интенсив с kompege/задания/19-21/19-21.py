def f(s,b,c,m):
    if s+b>76:return c%2==m%2
    if c==m:return 0
    h=[f(s+1,b,c+1,m),f(s*2,b,c+1,m),f(s,b+1,c+1,m),f(s,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for a in range(1,69):
    for m in range(9):
        if f(a,7,0,m):
            print(a,m)
            break