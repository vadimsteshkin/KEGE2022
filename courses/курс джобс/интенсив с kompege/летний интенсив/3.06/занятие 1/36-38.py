def f(a,b,c,m):
    if a+b>79:
        return c%2==m%2
    if c==m:return 0
    h=[f(a+b,b,c+1,m),f(a,b+a,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for b in range(1,60):
    for m in range(1,8):
        if f(20,b,0,m):
            print(b,m)
            break