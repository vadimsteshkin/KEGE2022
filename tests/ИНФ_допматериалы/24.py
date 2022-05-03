k=open('107_24.txt').readline()
for i in range(5):
    k=k.replace('AC','A C').replace('AA','A A').replace('BB','B B').replace('CC','C C').replace('CA','C A')
print(len(max(k.split(), key=lambda x:len(x)))//2)