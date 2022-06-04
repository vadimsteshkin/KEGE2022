k=3**72+6*3**50-7*3**26+2*3**15+155
s=set()
while k>0:
    s.add(k%9)
    k//=9
print(len(s))