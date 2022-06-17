def f(a,c,m):
    if a>39:return c%2==m%2
    if c==m:return 0
    h=[f(a+1,c+1,m),f(a+4,c+1,m),f(a*2,c+1,m),]
    return any(h) if c%2!=m%2 else all(h)
for a in range(1,39):
    for m in range(5):
        if f(a,0,m):
            print(a,m)
            break