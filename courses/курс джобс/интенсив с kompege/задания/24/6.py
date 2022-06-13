f=open('24_6.txt').readline().replace('XYZ',' ').split()
print(len(max(f,key=lambda x:len(x)))+4)