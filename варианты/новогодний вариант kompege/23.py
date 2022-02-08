from functools import *
@lru_cache
def f(s,e):
    if s<e:return 0
    if s==e:return 1
    else:return f(s-1,e) +f(s//2,e)
print(f(500,5)*f(5,0))