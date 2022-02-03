k=25**94+5**216-125
m=' '
while k>0:
    m+=str(k%5)
    k//=5
print(m.count('4'))