k=open('24_6.txt').readline()
m=0
for i in range(1,len(k)-3):
    if (k[i-1]!='S' or k[i]!='T') and k[i+1]=='O' and k[i+2]=='C' and k[i+3]=='K':
        
        m+=1
print(m)
#2 способ
print(k.count('OCK')-k.count('STOCK'))