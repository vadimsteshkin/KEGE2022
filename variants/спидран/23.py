def f(s,e):
    if s>e:
        return 0
    if s==e:return 1
    else:return f(s+1,e)+f(s+4,e)+f(s+5,e)
print(f(30,46))