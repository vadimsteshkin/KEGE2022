def f(s,b,c,m):
    if s+b>43:return c%2==m%2
    if c==m:return 0
    h=[f(s+b,b,c+1,m),f(s,s+b,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for a in range(1,33):
    for m in range(5):
        if f(a,11,0,m):
            print(a,m)
            break