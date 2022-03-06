k=5**20+5**10-5**13-5**3
s=0
while k>0:
    s+=k%5
    k//=5
print(s)