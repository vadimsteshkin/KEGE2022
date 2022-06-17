from functools import *
import time
import nu
s=time.time()
q=0
try:
    @lru_cache()
    def f(n):
        if n==0:return 5
        if n>0 and n%2==0:return  1+f(n/2)
        else:return  f(n//2)
except:
    ...
for i in range(1,1_000_000_001):
    if f(i)==7:
        q+=1
    if i%10_000_000==0:
        print(i)
e=time.time()
print(q,s-e)