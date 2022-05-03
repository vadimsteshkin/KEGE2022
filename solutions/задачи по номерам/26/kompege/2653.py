lst=[]
f=open('26_2653.txt')
for i in range(int(f.readline())):
    lst.append(int(f.readline()))
lst=sorted(lst)
for i in range(sum(lst),1,-1):