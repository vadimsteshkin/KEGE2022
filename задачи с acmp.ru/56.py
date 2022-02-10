_=int(input())
lst=[]
l=[]
ls=[]
for i in range(_):
    lst.append(input())
k=int(input())
for j in range(k):
    l.append(input())
p=int(input())
for u in range(p):
    ls.append(input())
print('Friends: '+lst.join(', '))
print('Mutual Friends: '+l.join(', '))
print('Also Friend of: '+ls.join(','))