f=open('24-178.txt').readline()

for i in range(len(f)-1):
    if f[i]<=f[i+1]:
        f=f.replace(f[i],'1',1)
    else:
        f=f.replace(f[i],'0',1)
print(len(max(f.split('0'),key=len)))
