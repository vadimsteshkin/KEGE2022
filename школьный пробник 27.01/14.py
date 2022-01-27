k=16**25+2**32-32
lst=' '
while k>0:
    lst+=str(k%4)
    k//=4
print(lst.count('3'))
print(lst)