# import array 

from array import *

val = array('i',[1,2,3,4,5,6])

for i in range(0,6):
    print(val[i],end=" ")

print('\n')
for x in val :
    print (x,end=",")

print('\n')
for i in range(0,len(val)):
    print(val[i],end=" ")




