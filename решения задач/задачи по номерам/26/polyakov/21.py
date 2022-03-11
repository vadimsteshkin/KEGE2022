_=open('26-k1.txt')
k=list(map(int,_.readline().split()))
lst=[]
for i in range(k[0]):
    lst.append(int(_.readline()))
lst=sorted(lst,reverse=True)
r=0
u=0
while u!=k[1]:
    r+=(lst[u]*0.2)
    u+=1
print(lst[k[1]],int(r))