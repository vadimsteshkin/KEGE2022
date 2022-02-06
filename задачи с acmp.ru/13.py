k=input().split()
m=0
o=0
for i in range(4):
    if k[0][i]==k[1][i]:
        m+=1
for j in k[0]:
    if k[0].count(j)==k[1].count(j) and k[0].index(j)!=k[1].index(j):
        o+=1
print(str(m)+" "+str(o))