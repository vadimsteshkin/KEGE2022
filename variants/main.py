k=[j for j in range(1,int(input())+2)]
lst=[]
m=0
i=1
while len(lst)<len(k):
    u=k[m:m+i][::-1]
    lst.extend(u)
    m+=i
    i+=1
print(*lst[0:len(k)-1])
