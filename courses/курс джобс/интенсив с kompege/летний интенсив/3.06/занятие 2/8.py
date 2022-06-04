f=open('8.txt').readline().replace('QW','Q W').split()
print(len(max(f,key=lambda x:len(x))))