k=49**7+7**21-7
q=0
while k>0:
    q+=(k%7==6)
    k//=7
print(q)