def f(s,e):
    if s>e:
        return 0 
    if s==e:
        return 1
    else:
        return f(s+1,e)+f(s*2,e)+f(s+3,e)
print(f(2,14)*f(14,24))