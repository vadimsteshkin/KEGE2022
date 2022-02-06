_=input()
k=[int(x) for x in input().split()]
m=0
ma=0
for i in k:
    if i>0:
        m+=1
    else:
        ma=max(m,ma)
        m=0
print(int(ma))