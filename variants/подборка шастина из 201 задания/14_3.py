k=5*216**1156-4*36**1147+6**1153-875
q=0
m=0
while k>0:
    q+=(k%6==5)
    m+=(k%6==0)
    k//=6
print(q-m)