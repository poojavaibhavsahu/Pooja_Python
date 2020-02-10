#write a program to check validation of email id
import re

str = "poojavaibhavsahoo14@gmail.com"

x = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str)

if (x):
    print("yes,it is valid")
else:
    print("Not valid")

