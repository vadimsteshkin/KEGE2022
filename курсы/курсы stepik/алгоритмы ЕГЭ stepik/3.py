s=0
s1=0
for i in range(int(input())):
    k=int(input())
    if k%2==0:
        s+=1
    else:
        s1+=1
print(abs(s1-s))