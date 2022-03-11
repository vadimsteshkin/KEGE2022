def f(s,e):
    if s>e or s==13:return 0
    if s==e:return 1
    else:return f(s+1,e)+f(s+4,e)
print(f(2,27))