k=open('24_10.txt').readline()
l=['AOUYEI']
q=0
m=0
k=k.split('.')
for i in k: 
    q=0
    for j in i:
        if j in l:
            q+=1
    if q<=7:
        m=max(len(i),m)
        print(i)
   
print(m)