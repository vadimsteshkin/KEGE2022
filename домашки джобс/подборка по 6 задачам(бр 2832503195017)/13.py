k=9**7+3**21-8
s=0
while k>0:
    s+=k%3
    k//=3
print(s)