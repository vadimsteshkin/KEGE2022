f=open('24-16.txt').readline().split('A')
lst1=[]
for i in range(len(f)-1):
    lst1.append(f[i]+f[i+1])
print(len(max(lst1,key=len))+1)