from functools import *
@lru_cache()
def f(s,p,c):
    if s>c and s==33:return 0
    if s==c:return 1
    else:
        if p==1:return f(s+1,0,c)+f(s+3,0,c)
        else:return f(s+1,0,c)+f(s+3,0,c)+f(s*2,1,c)
print(f(2,0,18)*f(18,0,51))