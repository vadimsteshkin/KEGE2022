f=open('27B_13.txt')
a=[10000000000]*11
tr=0
for i in range(int(f.readline())):
    k=int(f.readline())
    a[k%11]=min(a[k%11],k)
tr=0
for i in range(9):
    for j in range(i+1,10):
        for z in range(j+1,11):
            if (i+j+z)==11:
                tr=max(tr,a[i]+a[j]+a[z])
print(tr%11)