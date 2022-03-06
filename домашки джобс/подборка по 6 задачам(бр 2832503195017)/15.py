q=0
k=49**7+7**21-7
while k>0:
    if k%7==6:
        q+=1
    k//=7
print(q)