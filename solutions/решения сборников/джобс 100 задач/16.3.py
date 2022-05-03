from functools import *
@lru_cache()
def f(n):
    if n<10:return n
    if  n>9 and n%2==0:return g(n)-f(n-1)
    else:return f(n-1)+g(n-1)
@lru_cache
def g(n):
    if n<10:return n
    if n>9 and n%2:return f(n)+g(n-1)
    else:return g(n-1)-f(n-1)
print(f(40))