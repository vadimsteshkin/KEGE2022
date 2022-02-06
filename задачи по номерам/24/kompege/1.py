_=open('24_1.txt').read()
k=_
while 'YY'in k or 'ZZ' in k or "XX" in k:
    k=k.replace('XX', 'X X')
    k=k.replace('YY', 'Y Y')
    k=k.replace('ZZ', 'Z Z')
k=k.split()
print(len(max(k,key=len)))

#2 cпособ
m=1
ma=0
for i in range(len(_)-1):
    if _[i]!=_[i+1]:
        m+=1
    else:
        ma=max(m,ma)
        m=1
        

print(ma)