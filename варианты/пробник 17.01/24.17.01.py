k=open('24.txt').readline()
for i in range(len(k)-1):
    if k[i]>k[i+1]:
        k=k.replace(k[i]+k[i+1],k[i]+' '+k[i+1])
print(max(k,key=len))