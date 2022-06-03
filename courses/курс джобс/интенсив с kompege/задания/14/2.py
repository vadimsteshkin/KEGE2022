k=8**820-2**760+14
m=0
while k>0:
    m+=not(k%2)
    k//=2
print(m)