f=open('4.txt').readlines()
s=0
for j in f:
    for i in range(len(j)-4):
        if j[i]+j[i+2]+j[i+3]=='ZRO':
            s+=1
print(s)