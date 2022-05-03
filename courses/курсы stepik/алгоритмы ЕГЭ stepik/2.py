s=0
s1=0
for i in range(int(input())):
    k=int(input())
    if k%2==0:
        s+=k
    else:
        s1+=k
if s>s1:
    print('True')
if s<s1:
    print('False')
if s==s1:
    print("Equal")