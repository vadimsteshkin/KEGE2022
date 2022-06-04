def f(s,c,m):
    if s>73:return c%2==m%2
    if c==m:return 0
    h=[f(s+2,c+1,m),f(s+1,c+1,m),f(s*3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for a in range(1,72):
    for m in range(5):
        if f(a,0,m):
            print(a,m)
            break