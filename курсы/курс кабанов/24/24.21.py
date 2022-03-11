f=open('24_21.txt').readline()
i=1
while i*'DBAC'in f:
    i+=1
i-=1
o=i*'DBAC'
k=f.find(o)
print(i*4+3)