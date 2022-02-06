_=open('26.txt')
__=_.readline()
lst=[]
for i in range(int(__)):
    lst.append([int(x) for x in _.readline().split()])
lst=sorted(lst,reverse=True)

for i in range(len(lst)-1):
    if lst[i][0]==lst[i+1][0] and lst[i][1]-lst[i+1][1]==3:
        print(lst[i],lst[i+1])