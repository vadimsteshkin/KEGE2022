fi=open('27B.txt').readlines()
m=0
def f(a,b):
    if (a+b)%7==0:return 1
    return 0
s=sorted([int(x) for x in fi[1::]],reverse=True)
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        k=f(s[i],s[j])
        if k and s[i]+s[j]>m:
            print(s[i]+s[j])
            m=s[i]+s[j]


            