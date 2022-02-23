def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else:return f(s+1,e)+f(s+4,e)+f(s*4,e)
print(f(3,11)*f(11,27))