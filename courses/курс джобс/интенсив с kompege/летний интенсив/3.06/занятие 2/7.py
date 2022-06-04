f=open('7.txt').readline().replace('ZX','*').replace('ZY','*').replace('X',' ').replace('Y',' ').replace('Z',' ').split()
print(len(max(f,key=lambda x:len(x))))