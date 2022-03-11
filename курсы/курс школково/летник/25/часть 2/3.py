def p(n):
    k=str(n)
    if (int(k[0])+int(k[4])+int(k[2]))==  (int(k[1])+ int(k[3])):
            return 1
    return 0
q=0 
for i in range(10000,90001):
    if p(i):
        q+=1  
print(q)