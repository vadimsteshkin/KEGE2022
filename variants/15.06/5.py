a=[]
for _ in range(10000):
    b=bin(_)[2::]
    if b.count('1')%2==0:
        b='10'+b
    else:b='1'+b+'0'
    if int(b,2)<450:
        a.append(int(b,2))
print(max(a))