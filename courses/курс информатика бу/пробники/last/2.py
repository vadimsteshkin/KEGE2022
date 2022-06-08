from  itertools import *
for x,y,z in product([0,1], repeat=3):
    if (not x or y or not z) and ((not(x))==(not y or z)):print(x,z,y)