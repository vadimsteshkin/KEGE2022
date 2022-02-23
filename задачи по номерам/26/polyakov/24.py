_=open('26-k4.txt')
k=list(map(int,_.readline().split()))
lst=[]
for i in range(k[0]):
    lst.append(int(_.readline()))
lst=sorted(lst,reverse=True)
five=lst[::k[1]]
four=lst[k[1]:(k[1]*2)]
print(sum(four)/len(four),sum(five)/len(five))