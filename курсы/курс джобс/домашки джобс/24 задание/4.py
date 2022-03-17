k=open('24_4.txt').readline()
k=k.replace('A',' A ')
k=k.replace('E',' E ').split()
print(len(max(k,key=lambda x: len(x))))