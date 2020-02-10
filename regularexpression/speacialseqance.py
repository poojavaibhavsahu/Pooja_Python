import re
str = "the rain in spain"
#cheack if "ain" is present in the world or a string
x=re.findall(r"ain\b",str)
if(x):
    print("yes,there is at least one match!")
else:
    print("nomatch")