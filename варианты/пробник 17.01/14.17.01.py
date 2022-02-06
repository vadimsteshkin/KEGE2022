m=3*64**1073-1*16**1131+4**1173-484
f=m
k=set()
while m>0:
    k.add(m%4)
    m//=4
for i in k:
    print(i,str(f).count(str(i)))
print(206-172)