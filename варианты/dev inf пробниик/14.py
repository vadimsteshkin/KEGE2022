k=16**820-2**761+14
lst=[]
while k>0:
    lst.append(k%4)
    k//=4
print(lst.count(0),lst)