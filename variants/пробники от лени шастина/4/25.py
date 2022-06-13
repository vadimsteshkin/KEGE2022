a=['']
a.extend([str(i) for i in range(100)])
for i in a:
    for j in range(1,5):
        a.append(i*j)
a=set(a)
print(a)
k=[]