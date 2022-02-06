k=open('24_7.txt').readline()
a='ASDFGHJKLZXCVBNMQWERTYUIOP'
for i in a:
    k=k.replace(i,' ')
print(max(int(x) for x in  k.split()))