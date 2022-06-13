f=open('24.txt').readline()
f=f.replace('AB','*').replace('AC','*')
q=1
while '*' *q in f:
    q+=1
print(q-1)