k=open('24_9.txt').readline()
q=0
m=0
k=k.split('.')
for i in k: 
    q=0
    for j in i:
        if j =='A':
            q+=1
    if q>2:
        m=max(len(i),m)
   
print(m)