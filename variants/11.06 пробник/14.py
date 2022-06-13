k=2197**50-169**35-26
q=0
while k>0:
    if k%13==12:
        q+=1
    k//=13
print(q)