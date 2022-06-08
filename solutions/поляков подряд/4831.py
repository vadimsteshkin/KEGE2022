def f(s,p,c,m):
    if s>=140:return c%2==m%2
    if c==m:return 0
    if p=='':h=[f(s+2,'2',c+1,m),f(s*3,'3',c+1,m),f(s+1,'1',c+1,m)]
    if p=='1':h=[f(s+2,'2',c+1,m),f(s*3,'3',c+1,m)]
    if p=='2':h=[f(s+1,'1',c+1,m),f(s*3,'3',c+1,m)]
    if p=='3':h=[f(s+2,'2',c+1,m),f(s+1,'1',c+1,m)]
    return any(h) if c%2!=m%2 else all(h)
for i in range(1,140):
    for m in range(7):
        if f(i,'',0,m):
            print(i,m)
            break