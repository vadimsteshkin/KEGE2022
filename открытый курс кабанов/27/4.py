k=open('27A_4.txt')
k5_n=0
k5_ch=0
k1=0
k0=0
for i in range(int(k.readline())):
    m=int(k.readline())
    if m%5==0 and m%2==0:k5_ch+=1
    elif m%5==0 and m%2==1:k5_n+=1
    elif m%5!=0 and m%2==0:k1+=1
    elif m%5!=0 and m%2==1:k0+=1
print(k5_ch*k5_n + k1*k5_n + k0*k5_ch)