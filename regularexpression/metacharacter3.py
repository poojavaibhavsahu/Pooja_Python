#check if the string contains "a" followd by exctly two"i" charater:
import re
str="the rain in spain all\s in the plain!"
x=re.findall("al{2}",str)
if(x):
    print("yes,there is at least one match!")
else:
    print("no match")
#cheack if the string contains either "falls" or"stays" :
import re
str="the rain in spain falls in the plain!"
x=re.findall("falls|stays",str)
if(x):
    print("yes,there is at least one match!")
else:
    print("no match")

