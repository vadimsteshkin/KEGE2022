f=[int(x) for x in open('17.txt')]
lst=[]
for i in range(len(f)-1):
    m=f[i]+f[i+1]
    if m%2==0 and m%10!=6:
        lst.append(m//2)
print(len(lst),max(lst))
print(int('201',8)-int('1111110',2))
print(sum([int(input()) for _ in range(int(input()))][0:len]))