f=open('27B_5.txt')
k=0
for i in range(int(f.readline())):
    m=int(f.readline())
    if m%19==0:
        k+=1
        print(m)
print(k*(k-1)*(k-2)//6)