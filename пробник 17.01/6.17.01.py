o=0
for x in range(1,99999):
    s=5*(x//10)
    n=1
    while s<300:
        s+=28
        n*=3
    if n==243:
        o+=1
print(o)
