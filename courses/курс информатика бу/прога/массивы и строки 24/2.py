f=open('24zadachi__kma.txt').readline()
i=1
while 'Z'*i in f:
    i+=1
print(i-1)