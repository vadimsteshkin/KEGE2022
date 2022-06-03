from functools import *
@lru_cache()
def f(n):
    if n<=2:return 1
    if n>2 and n%2:
        return f(n-1)-n
    else:return f(n-2)+g(n-1)+2
@lru_cache()
def g(n):
    if n<=0:
        return 2
    if n>0 and n%2:return f(n-1)-2*g(n-2)
    else:return 2*(n-2)-2*g(n-1)
print(f(96))