k=open('24.txt').readline()
k=k.replace('D', ' ').split()
lst=[]
for i in range(len(k)-1):
    lst.append(k[i]+k[i+1])
print(len(max(lst,key=len))+1)