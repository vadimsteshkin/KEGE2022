def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else:return f(s+3,e)+f(s+4,e)+f(s*2,e)
print(f(3,22)*f(22,35))