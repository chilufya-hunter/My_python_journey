#(1) NONE
#if a variable isnt assigned a value it is NONE
#(2)NUMERIC 
#we have muiltple types of numbers INT FLOAT COMPLEX BOOL
#EXAMPLE FLOAT
import string
from typing import List, Type


num = 2.5
type(num)

#INT 
num = 2

#complex
num = 6+7j

#converting a float into a INT
a = 4.7
b =int(a)
print(b)
z = 8

c = complex(z,b)
print(c)

#BOOLEN bool true or false 
bool = a<z
print(bool)

#sequence(list,tuple,set,string,range)
list = [33,66,89,564,8,4]

set = {56,54,87,54,23}

tuple = (43,6,53,6,445,33,56)

string = 'money'

range(0,19)

#dictionary
#for every value we assign a key
d = {'chilu':'bmw','john':'ford','noah':'vitz'}
print(d)
#to reveal keys
d.keys()

till=d['john']
print(till)
#to get a value
tell = d.get('noah')
print(tell)
