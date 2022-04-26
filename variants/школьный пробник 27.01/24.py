f=open('zadanie_24.txt').readline()
for i in range(1,100):
    if 'C'*i in f:
        print(i)