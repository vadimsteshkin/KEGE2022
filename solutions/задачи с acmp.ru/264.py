_=input()
k=[int(x) for x in input().split()]
m=0
ma=0
for i in k:
    if i>=1:
        k[k.index(i)]='a'
k=''.join([str(i) for i in k])
i=1
while 'a'*i in k:
    i+=1
print(i-1)