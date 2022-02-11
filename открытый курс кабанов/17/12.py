k=[int(x) for x in open('17_12.txt')]
lst=[]
for i in range(len(k)-1):
    if k[i]+k[i+1]>=100 and (min(k[i],k[i+1])<0):
        lst.append(k[i]*k[i+1])
        print(k[i]*k[i+1])
print(len(lst),max(lst))