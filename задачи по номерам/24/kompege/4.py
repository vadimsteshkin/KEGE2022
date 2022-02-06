k=open('24_4.txt').readline()
m=0
for i in range(len(k)-2):
    if k[i]+k[i+1]+k[i+2]=='TIK' or k[i]+k[i+1]+k[i+2]=='TOK':
        m+=1
print(m)
#2 способ
print(k.count('TIK')+k.count('TOK'))