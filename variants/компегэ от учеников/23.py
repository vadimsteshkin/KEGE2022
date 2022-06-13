from functools import *
o=[2**int(i) for i in range(100)]

@lru_cache()
def pr(s):
    for i in range(2,int(pow(s,0.5)+1)):
        if s%i==0:return 0
    return 1
p=[i for i in range(1,10000) if pr(i)]
print(p)
@lru_cache()
def prime(s):
    global p
    for i in range(s,10000000000):
        if i in p:return i+s
@lru_cache()
def two(s):
    global o
    for i in o:
        if i>s:return s+i
@lru_cache()
def n(s):
    k=str(s)[-1]
    if k!='0':
        return s+int(k)
    return s
try:
    def f(s,e):
        if s>e or s==3 or s==14:return 0
        if s==e:return 1
        else: return f(two(s),e)+ f(prime(s),e)+f(n(s),e)
except RecursionError:
    ...
print(f(2,1024)*f(1024,3072))