k=open('27-B_1.txt')
m=0
b=[]
for _ in range(int(k.readline())):
    m1=list(map(int,k.readline().split()))
    m+=max(m1)
    b.append(max(m1) - min(m1))
k.close()
b=sorted(b)
for i in b:
    if (m-i)%3!=0:
        print(m-i)
        break
#127127 399762080
