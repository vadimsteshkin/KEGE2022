from functools import *
@lru_cache()
def f(x):
    if x<5:
        return x%3
    if x %2==0 and x>4:
        return 2*f(x-2) + x*2
    else:
        return f(x-2)+x%4
for i in range(1,10000):
    m=f(i)
    if m<=1500:
        print(i)