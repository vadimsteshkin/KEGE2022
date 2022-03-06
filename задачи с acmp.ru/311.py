from functools import *
s=0
for i in range(3):
    print(reduce(lambda x,y:x*y,range(1,i+1)))
print(s)