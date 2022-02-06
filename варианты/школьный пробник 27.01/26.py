k=[x for x in open('zadanie_26.txt')]
m=int(k[0].split()[0])
k=sorted(list(map(int,k[1::])),reverse=True)
lst=0
i=0
while lst<m:
    lst+=k[i]
    i+=1
print(lst,i)