alpha='abcdefghijklmnopqrstuvwxyz'*7
k=input()
s=''
k=k.replace('10','1 0').split()
for i in k:
    s+=alpha[i.count('0')]
print(s)