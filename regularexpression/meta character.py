import re
str ="python is programming language 90 78"
#find all lower case character alphabeticaly between "a" and "m":
x=re.findall("[a-m]",str)
print(x)
#find all digit characterr:
x=re.findall("\d",str)
print(x)
str1="hello world"
#search for a seqance that strts with "he",followeed by two (any) charater,
#and an"o":
x= re.findall("he..o",str1)
print(x)
x1=re.findall("w...d",str1)
print(x1)


