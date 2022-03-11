k=open('24_5.txt').readline()
m=0
for i in range(1,len(k)-4):
    if k[i-1]!='J' and k[i]=='B' and k[i+1]=='O' and k[i+2]=='S' and k[i+3]=='S' and k[i+4]!='J':
        m+=1
print(m)
#2 способ
print(k.count('BOSS')-k.count('BOSSJ')-k.count('JBOSS')+k.count('JBOSSJ'))