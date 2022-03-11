k=[int(x) for x in open('17_16.txt')]
s=[int(x) for x in k if x%17==0]
e=[int(x) for x in k if x%11==0]
if len(e)>len(s):
    print(len(e),min(e))
else:
    print(len(s),mins)