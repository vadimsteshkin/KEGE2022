f=open('24_4.txt').readline().replace('A',' ').replace('E',' ').split()
print(len(max(f,key=lambda x:len(x))))