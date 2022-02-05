a=list('QWERTYUIOPASDFGHJKLZXCVBNM')
k=input()
for i in a:
    k=k.replace(i,' '+i)
k=k.split()
if len(max(k,key=len))>4 or len(max(k,key=len))==1 or en(max(k,key=len))==0:
    print('No')
else:print('Yes')