k=open('zadanie_27_.txt')
lst=[]
ma=100000000000000000000000000000000
for _ in range(int(k.readline())):
    lst.append(int(k.readline()))
for k in range(len(lst)-5):
    m=pow(lst[k],2)+pow(min(lst[k+5::]),2)
    ma=min(ma,m)
print(ma)
#11009