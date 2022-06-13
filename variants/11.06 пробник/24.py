=open('24.txt').readline().replace('BB','*').replace('DD','*')
q=1
while q*'*' in f:
    q+=1
print(q-1)
