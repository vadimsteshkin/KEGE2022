f=open('24_5.txt').readline()
q=0
s=0
for i in f:
    s+=1
    if i=='f':
        q+=1
    if q==123:
        print(s)
        break