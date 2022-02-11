k=open(('24_14.txt')).readline()
k=k.replace('DD','D D').split()
print(len(min([i for i in k if i!='DD'],key=len))-1)