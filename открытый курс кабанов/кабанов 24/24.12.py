_=open('24_12.txt').readline()
k=[int(i) for i in _[0:-1]]
m=' '
for i in range(1,len(k)):
    if k[i]>k[i-1]:
        m+='1'
    else:
        m+='0'
m=m.replace('0',' ').split(' ')
print(max(list(m),key=len)+1)