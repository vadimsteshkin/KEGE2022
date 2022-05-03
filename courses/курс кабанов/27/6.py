f=open('27B_6.txt')
a=[0 for i in range(131)]
for i in range(int(f.readline())):
    a[int(f.readline())%131]+=1
c=(a[0]*(a[0]-1))//2
for i in range(1,65+1):
    c+=a[i]*a[131-i]
print(c)