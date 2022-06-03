k=7**21+49**13-7**10
s=0
while k>0:
    if k%7==6:
        s+=1
    k//=7
print(s)