def f(s,e):
    if s>e or s==25:return 0
    if s==e:return 1
    else:return f(s+1,e)+f(2*s+1,e)
print(f(1,31))