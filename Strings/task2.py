#Program to count the number of l in String

count = 0

str1="Hello World"

for letter in str1:

    if(letter == 'l'):
        count += 1
print(count,'letters found')