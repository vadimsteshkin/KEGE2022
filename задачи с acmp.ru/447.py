from functools import *
print(str(reduce(lambda x,y:x*y,range(1,int(input())+1))).replace('0','')[-1])
