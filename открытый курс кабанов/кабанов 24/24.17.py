f=open('24-17.txt').readline().split('D')
lst1=[]
for i in range(len(f)-2):
    lst1.append(f[i]+f[i+1]+f[i+2])
print(len(max(lst1,key=len))+2)
