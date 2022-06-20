f=open('24.txt').readline()
for i in range(2):
    f=f.replace('PR','P R').replace('R P','R P')
print(len(max(f.split(),key=len)))