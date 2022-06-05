k=[int(i) for i in open('17_3.txt')]
n=max(k)
m=[i for i in k if n%2==i%2]
print(len(m),min(m))