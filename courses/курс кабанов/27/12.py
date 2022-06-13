f=open('27B_12.txt')
a=[]
n=0
ch=0
tr1=0
tr=0
for i in range(int(f.readline())):
    k=int(f.readline())
    if k%23==0 and k %2:tr1=max(tr1,k)
    if k % 23 == 0 and k % 2==0: tr = max(tr, k)
    if k % 23 != 0 and k % 2==0: ch = max(ch, k)
    if k % 23 != 0 and k % 2: n = max(n, k)
print(tr,tr1,n,ch)
print(max(tr1+n,tr+ch))