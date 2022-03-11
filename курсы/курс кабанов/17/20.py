
k=[int(x) for x in open('17_20.txt')]
j=10000000000000000
q=0
s=0
for i in k:
    if i%35==0:
        s+=sum([int(x) for x in str(i)])
for i in range(len(k)-1):
    n=k[i]
    m=k[i+1]
    if (n>s and m<=s and m%16==15 and m//16%16==14) or (m>s and n<=s and n%16==15 and n//16%16==14):
        q+=1
        j=min(j,k[i]+k[i+1])
print(q,j)