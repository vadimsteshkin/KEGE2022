def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else: return f(s+1,e)+ f(4*s,e)+f(3*s,e)
print(f(1,17))