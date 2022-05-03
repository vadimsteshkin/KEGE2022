f=open('27A_8.txt')
a5=[0 for i in range(80)]
a=[0 for i in range(80)]
for i in range(int(f.readline())):
    k=int(f.readline())
    if k<=50000:
        a[k%80]+=1
    else:a5[k%80]+=1
c=a[0]*a5[0]+a5[0]*(a5[0]-1)//2+a[40]*a5[40]+a5[40]*(a5[40]-1)//2
for i in range(1,40):
    c+=a[i]*a5[i]+a5[i]*(a5[i]-1)//2+a[80-i]*a5[80-i]+a5[80-i]*(a5[80-i]-1)//2
print(c)