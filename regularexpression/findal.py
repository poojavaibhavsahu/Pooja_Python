 #this methid returns a list containning a list of
# all matches of a pattrn with in the string
import re
str1 = 'how are you. how how is eveything'
matchs = re.findall("how",str1)
print(matchs)