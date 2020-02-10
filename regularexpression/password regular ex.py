import re
str="pooja.sahoo123@"
a=re.search(r"(^[A-Za-z0-9.@]{8})",str)
if(a):
    print("valid")
else:
    print("not valid")
