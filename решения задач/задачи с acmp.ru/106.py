k=''
for i in range(int(input())):
    k+=input()
print(min(k.count('1'),k.count('0')))