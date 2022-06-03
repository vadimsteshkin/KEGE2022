al='QWERTYUIOPASDFGHJKLZXCVBNM'
lst=[]
k=open('24.txt').readline()
for i in al:
    lst.append(k.count(i))
print(k.count('EI')+k.count('IE'))
print(lst.index(max(lst)),lst.index(min(lst)))