import re
str = "the rain in spain falls mainly in the plan ai!"
#cheack if the string contains "ai" followed by 0 or more character:
x=re.findall("ai*",str)
if(x):
    print("yes,there is a least one match")
else:
    print("no match")

#cheack if the string contains "ai" followed by 1 or more character:

x1 = re.findall("ai+", str)
if (x1):
    print("yes,there is a least one match")
else:
    print("no match")