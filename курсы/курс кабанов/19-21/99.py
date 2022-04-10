q=0
s=True
p1=p2=False
k=sorted(list(map(int,input().split())))
for i in range(len(k)-1):
    if abs(k[i]-k[i+1])!=1:
        s=False
m=False
for j in range(len(k)): 
    if k[j]==1:
        k[j]==14
    if k.count(k[j])==3:
        m=True
    if k.count(k[j])==4:
            p2=True
if max(k)==min(k):
    print('Шулер')
elif p2:
    print('Каре')
elif (k.count(max(k))==3 and k.count(min(k))==2) or (k.count(max(k))==2 and k.count(min(k))==3):
    print('Фулл Хаус')
elif s:
    print("Стрит")
elif m:
    print('Сет')
elif len(set(k))==3:
    print('Две пары')
elif len(set(k))==4:
    print('Пара')
else:
    print('Старшая карта')