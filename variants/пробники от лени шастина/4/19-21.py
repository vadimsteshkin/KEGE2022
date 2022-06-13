def f(s,c,m):
    if s>39:return c%2==m%2
    if c==m:return 0
    h=[f(s+1,c+1,m),f(s+3,c+1,m),f(s*2,c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for i in range(40):
    for m in range(7):
        if f(i,0,m):
            print(i,m)
            break