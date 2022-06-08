def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else:return f(s+2,e)+f(s*2,e)
print(f(1,18)*f(18,52))
