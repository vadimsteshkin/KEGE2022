def f(s,c):
    if s>c or s==14:return 0
    if s==c:
        return 1
    else:return f(s+1,c)+f(s+3,c)
print(f(2,9)*f(9,18))