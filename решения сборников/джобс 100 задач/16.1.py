from functools import *
@lru_cache()
def f(x):
    if x==1:
        return 5
    if f(x-1) %2==0 and x>1:
        return f(x-1) + x//2
    else:
        return f(x-1)+x**2-1
print(f(40))