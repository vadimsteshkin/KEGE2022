_=int(input())
k=[int(x) for x in input().split()]
ma=k.index(max(k))
mi=k.index(min(k))
s=k[mi+1:ma]
_=1
for  i in s:
    _*=i
o=sum([x for x in k if x>0])
print(o,_)