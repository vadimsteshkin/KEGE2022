f=open('24_20.txt').readline()
i=1
while i*'XYZ'in f:
    i+=1
i-=1
print(3*i)
