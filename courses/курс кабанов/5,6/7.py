o=0
for j in range(1,80000):
    n=bin(j)[2::]
    for i in range(2):
        k=sum([int(i) for i in n])
        n+=str(k%2)
    if int(n,2)<80:
        o+=1
print(o)