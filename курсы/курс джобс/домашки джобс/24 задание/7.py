k=open('24_7.txt').readline()
k=k.replace('ad','a d')
k=k.replace('da','d a').split()
print(len(max(k,key=lambda x: len(x))))