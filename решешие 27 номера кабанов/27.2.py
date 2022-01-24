k=open('27-B_2.txt')
lst=[]
lst1=[]
o=0
for i in range(int(k.readline())):
    m=int(k.readline())
    if m%2==0:
        lst.append(m)
    else:
        lst1.append(m)
lst+=lst1
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if (lst[i]-lst[j])%13==0 and (lst[j] * lst[i])%2==0:
            o+=1
print(o)