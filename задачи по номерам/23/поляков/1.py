def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else: return f(s+1,e)+ f(2*s,e)
print(f(1,16))