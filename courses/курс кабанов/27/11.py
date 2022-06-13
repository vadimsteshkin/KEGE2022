f=open('27B_11.txt')
a=[]
n=1000000000000000000
tr=10000000000
for i in range(int(f.readline())):
    k=int(f.readline())
    if k%31==0:tr=min(tr,k)
    else:n=min(n,k)
print(tr*n)