k=6*343**1156-5*49**1147+4*7**1153-875
q=''
while k>0:
    q+=str(k%7)
    k//=7
print(sum(int(i) for i in q))