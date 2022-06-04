def f(s,p,c):
    if s>c or p>3:return 0
    if s==c:
        return 1
    else:return f(s+2,p,c)+f(s*3,p+1,c)+f(s*5,p+1,c)
print(f(2,0,200))