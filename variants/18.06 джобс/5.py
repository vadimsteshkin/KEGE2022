m=[]
for i in range(1,100000):
    b=bin(i)[2::]
    if i%2==0:
        b='1'+b+'0'
    else:b='11'+b+'10'
    if sum((int(j) for j in b))>17:
        m.append(int(b,2))
        print(min(m))
print(min(m))