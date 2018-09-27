###### this is the second .py file ###########

####### write your code here ##########
string = raw_input("enter the string here")
key1= int(input("enter the value of key1="))
key2= int(input("enter the value of key2="))
key3= int(input("enter the value of key3="))
length= len(s)
from array import *
a= array('c', [])
b= array('c', [])
c= array('c', [])
for i in range(length):
if(string(i)>= 'a' and string(i)<='i'):
a.append(string(i))
if(string(i)>= 'j' and string(i)<='r'):
b.append(string(i))
if(string(i)>= 's' and string(i) <='z' and string(i)== '_'):
c.append(string(i))
print a
print b
print c
