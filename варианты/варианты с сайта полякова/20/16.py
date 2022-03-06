from functools import *
try:
    @lru_cache
    def f(n):
        if n<=5:
            return n
        if n>5 and n%5==0:
            return f(n/5+1)+n
        if n>5 and n%5!=0:
            return n+f(n+6)
except:
    ...
for i in range(1,10000):
    if f(i)>1000:
        print(i)
        break