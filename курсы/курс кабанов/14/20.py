q=0
for i in range(2,3600):
    if len(bin(i)[2::])>=5 and i<625 and i%16==12:
        q+=1
print(q)