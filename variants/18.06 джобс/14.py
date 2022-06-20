k=5**94+25**49-130
q=0
while k>0:
    q+=(k%5==4)
    k//=5
print(q)