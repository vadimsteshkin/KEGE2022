k=[int(x) for x in open('17_11.txt')]
lst=[]
for i in range(len(k)-3):
    if k[i]+k[i+1]+k[i+2]+k[i+3]>+100 and(k[i]<0 or k[i+1]<0 or k[i+2]<0 or k[i+3]<0):
        lst.append(k[i]*k[i+1]*k[i+2]*k[i+3])
print(len(lst),sorted(lst)[-1])