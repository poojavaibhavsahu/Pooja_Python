import re
str = "the rain in spain"
#cheak return space character
x=re.findall("\s",str)
print(x)
if(x):
    print("yes,there is at least one match!")
else:
    print("nomatch")

#check if the string startss with the
import re

str = "the rain in spain"

x = re.findall("\Athe", str)
print(x)
if (x):
    print("yes,there is at least one match!")
else:
    print("nomatch")


#cheack if he string ends with "spain":
import re

str = "the rain in spain"

x = re.findall("spain\Z", str)
print(x)
if (x):
    print("yes,there is at least one match!")
else:
    print("nomatch")

