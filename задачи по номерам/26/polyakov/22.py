_=open('26-k2.txt')
k=list(map(int,_.readline().split()))
lst=[]
for i in range(k[0]):
    lst.append(int(_.readline()))
lst=sorted(lst,reverse=True)
lst=lst[k[1]:(len(lst)-k[1]+1)]
print(max(lst),sum(lst)//len(lst))