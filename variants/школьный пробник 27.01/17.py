f=[int(x) for x in open('zadanie_17.txt')]
lst=[]
for i in range(len(f)-1):
    if hex(f[i])[-1]=='e' or hex(f[i+1])[-1]=='e':
        lst.append(f[i]+f[i+1])
print(len(lst),max(lst))