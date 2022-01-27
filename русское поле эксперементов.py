f=open('9.txt').readlines()
o=0
for i in range(len(f)):
    k=sorted(list(map(int,f[i].split('\t'))))
    if k[2]<(k[1]+k[0]):
        o+=1
print(o)