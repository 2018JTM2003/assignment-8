###### this is the second .py file ###########

####### write your code here ##########

#!/usr/bin/python

string = raw_input("enter the string here")  # Takes the string as input
key1= int(input("enter the value of key1=")) # takes the valus of key1
key2= int(input("enter the value of key2=")) # takes the valus of key2
key3= int(input("enter the value of key3=")) # takes the valus of key3
length= len(s) # it tarcks the length of the string
from array import *
a= array('c', []) #appends the first character of the string 
b= array('c', [])
c= array('c', [])
for i in range(length):   #using the for loop
if string(i)>= 'a' and string(i)<='i' : # defining conditions
a.append(string(i))
if string(i)>= 'j' and string(i)<='r' :
b.append(string(i))
if string(i)>= 's' and string(i) <='z' and string(i)== '_':
c.append(string(i))
print a #prints value of a
print b #prints value of a
print c #prints value of c
