k=open('27_B.txt')
lst=[]
lst1=[]
for i in range(int(k.readline())):
    lst.append(int(k.readline()))
for i in range(len(lst)):
    if sum(lst[i::])%89==0 and sum(lst[i::])%(len(lst)-i)==0:
        lst1.append([sum(lst[i::]),len(lst[i::])])
print(sorted(lst1,reverse=True))
