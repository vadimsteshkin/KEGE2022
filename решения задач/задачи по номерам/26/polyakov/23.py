_=open('26-k3.txt')
k=list(map(int,_.readline().split()))
lst=[]
for i in range(k[0]):
    lst.append(int(_.readline()))
lst=sorted(lst,reverse=True)
print(lst[k[2]+k[1]-1],lst[k[1]-1])