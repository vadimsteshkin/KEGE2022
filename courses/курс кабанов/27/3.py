k=open('27B_3.txt')
k65=0
k5=0
k13=0
k0=0
for i in range(int(k.readline())):
    m=int(k.readline())
    if  m%65==0:k65+=1
    elif m%13==0:k13+=1
    elif m%5==0: k5+=1
    else:k0+=1
print(k65*(k65-1)//2+k5*k13+k65*(k13+k5+k0))