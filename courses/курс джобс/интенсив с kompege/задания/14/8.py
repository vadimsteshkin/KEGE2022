
for x in range(6,100):
    k=73786976294837157984
    k=k-x
    s=0
    while k>0:
       s+=k%4
       k//=4
    if s==71:
        print(x)
        break