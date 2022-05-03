k=[int(x) for x in open('17_11.txt')]
lst=[]
for i in range(len(k)-3):
    if k[i]>k[i+1]>k[i+2]>k[i+3] and k[i]-k[i+3]>1000:
        lst.append(k[i]+k[i+1]+k[i+2]+k[i+3])
print(len(sorted(lst)),sorted(lst)[0])