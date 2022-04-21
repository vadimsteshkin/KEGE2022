a=set()
b={1,3,5,7,9,11}
c={3,6,9,12}
for i in range(1000):
    if ((i in b)<=(not(i in c)))==0:
        a.add(i)
print(a)