q=0
k=open('24_5.txt').readline()
for i in range(len(k)):
    if k[i]=='f':
        q+=1
    if q==123:
        break
print(i+1)