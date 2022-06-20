f=[int(i) for i in open('test.txt')][1::]
print(f)
q=0
for i in range(len(f)-20):
    for j in range(i,i+20):
        if sum(f[i:j+1])%39==0:
            q+=1
            print(f[i:j+1],sum(f[i:j+1]))

print(q)