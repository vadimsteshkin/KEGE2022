def f(s,p,c,m):
    if s>=20:return c%2==m%2
    if c==m:return 0
    if p==0:
        h=[f(s+2,p,c+1,m),f(s*2,p,c+1,m),f(s*2,p+1,c+1,m),f(s+2,p+1,c+1,m),]
    else:h=[f(s+2,p,c+1,m),f(s*2,p,c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for i in range(1,19):
    for m in range(7):
        if f(i,0,0,m):
            print(i,m)
            break