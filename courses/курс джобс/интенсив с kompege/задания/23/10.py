from functools import *
@lru_cache()
def f(s,e):
    if s>e:return 0
    if s==e:return 1
    else:return f(s*2,e)+f(s*2+1,e)
for i in range(2,100000):
    k=f(1,i)
    if k==15:
        print(i,k)