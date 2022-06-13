f=open('24.txt').readline().replace('ZYX','*').replace('ZXY','*')
q=1
while '*' *q in f:
    q+=1
print(q-1)