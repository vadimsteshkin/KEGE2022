k=sorted([int(i) for i in open('174.txt').readlines()])
print(k)
for i in k:
    if i%2!=0:
        k.remove(i)
print(len(k),k[0])
