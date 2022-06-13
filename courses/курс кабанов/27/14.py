f=open('27A_14.txt')
a=[[] for i in range(11)]
tr=0
for i in range(int(f.readline())):
    k=int(f.readline())
    a[k%11].append(k)
m=[]
for i in range(11):
    a[i].sort()
    m+=a[i][:4]
for i in r