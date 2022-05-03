q=0
for i in range(123457,124690):
    if (int(str(i)[3])%6==0) or  (int(str(i)[5])%6==0):
        q+=1
print(q)