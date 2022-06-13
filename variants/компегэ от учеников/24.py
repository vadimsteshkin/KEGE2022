f=open('24_ip.txt').readlines()
q=0
a=[]
for i in range(10):
    for j in range(10):
        a.append('195.2'+str(i)+'.1'+str(j)+'5.14')
print(a)
print(sum([1 for i in f if i in a]))