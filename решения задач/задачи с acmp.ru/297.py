k=['0','6','8','9']
p=[1,1,2,1]
_=input()
s=0
for i in _:
    if i in k:
        s+=p[k.index(i)]
print(s)