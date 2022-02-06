k=open('24_15.txt').read()
lst=[]
lst1=[]
while k.find('D')!=-1:
    lst.append(k.find('D'))
    k=k.replace('D',' ',1)
for i in range(len(lst)-1):
    lst1.append(lst[i+1]-lst[i])
print(str(lst1))