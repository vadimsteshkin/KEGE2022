#количество пар элементов произыедение которых кратно 11
n=file()
e=0
ne=0
for i in n:
    if e%11==0:e+=1
    else:ne+=1
print(e*(e-1)//2+e*ne)