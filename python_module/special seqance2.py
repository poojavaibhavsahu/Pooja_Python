#return a match at every word character  #character from a ti z,digit from 0_( and underscore_ character:
import re
str = "the rain in _spain "
#cheack if "ain" is present in the world or a string
x=re.findall(r"\w",str)
print(x)
if(x):
    print("yes,there is at least one match!")
else:
    print("nomatch")

    #character not between a and z like"!","?"whitw space :return a match non word character
import re

str = "the rain in _spain "

x = re.findall(r"\W", str)
print(x)
if (x):
    print("yes,there is at least one match!")
else:
    print("nomatch")

