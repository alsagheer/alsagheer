#write a pyton program to construct the following pattern using a nested loop number expected output

from __future__ import print_function
x=input("enter the value: ")
for x in range (1,x+1):
    y=x
    while y>0:
       print (end=str(x))
       y=y-1
    print ("")
   
