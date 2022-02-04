o=0
def F( n ):
  global o
  o+=1
  if n >= 1:
       o+=1
       F(n-1)
       F(n-2)
F(10)

print(o)