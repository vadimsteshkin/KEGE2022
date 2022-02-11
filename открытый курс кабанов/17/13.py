k=[int(x) for x in open('17_13.txt')]
lst=[]
q=0
for i in range(len(k)-1):
    if 50<=(abs(k[i])+abs(k[i+1]))<=200:
        lst.append(k[i])
        lst.append(k[i+1])
        print(k[i],k[i+1])
        q+=1
print(q,min(lst))