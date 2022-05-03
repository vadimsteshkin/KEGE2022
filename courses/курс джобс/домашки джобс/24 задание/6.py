k=open('24_6.txt').readline()
k=k.replace('XYZ',' ').split()
print(len(max(k,key=lambda x: len(x)))+4)