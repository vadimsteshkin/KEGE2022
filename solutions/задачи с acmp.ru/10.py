lst=[]
k=[int(x) for x in input().split()]
for x in range(-32768,32768):
    if k[0]*x**3+k[1]*x**2+k[2]*x+k[3]==0:
        lst.append(x)
print(*lst)