from functools import *
@lru_cache(None)
def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else:return f(s*2,e)+f(s*2+1,e)
for i in range(10000):
    if f(1,i)==15:
        print(i)