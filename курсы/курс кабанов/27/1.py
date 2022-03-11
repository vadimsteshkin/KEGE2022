k=open('27B_1.txt')
lst_ch=[]
lst_n=[]
for i in range(int(k.readline())):
    m=int(k.readline())
    if m%2==0:
        lst_ch.append(m)
    else:
        lst_n.append(m)
o=0
for _ in range(len(lst_n)):
    o+=_
for _ in range(len(lst_ch)):
    o+=_
print(o)