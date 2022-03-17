lst=[]
k=open('26_2686.txt')
for _ in range(int(k.readline())):
    x,y=map(int,k.readline().split())
    lst.append([x,y])
lst=sorted(lst)
l=[]
for x in range(len(lst)-1):
    if lst[x][0]==lst[x+1][0]:
        l.append(lst[x+1][1]-lst[x][1])    
    else:
        if len(l)>4 and max(l)==1:
            print(*lst[x])
            break
        l.clear()
    
