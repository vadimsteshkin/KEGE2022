k=[int(x) for x in open('17.txt')]
lst=[]
for i in range(len(k)-1):
    if (k[i]%5==0 and k[i]%3!=0) and (k[i+1]%5==0 and k[i+1]%3!=0):
        lst.append([k[i],k[i+1]])
print(lst)
print(len(lst),min([i for i in lst if sum(i)>0]))