s="hello how are you you."

print("First letter of String is in capital:",s.capitalize())

print("Counts the number of times string occurred:",s.count("you"))

print("Check the ending String:",s.endswith("you"))

print("Check the starting String:",s.startswith("hello"))


str = "Welcome to the ITView Progessive Learning"

str2 = str.find("the")
# Displaying result
print(str2)


print("to check in which index it is present",str.index("the"))

#removes any white space at beginning or ending
a = " Hello, World! "
print(a.strip())

print("Checks the length of the string:",len(a))

print("Returns the string in lowercase",a.lower())

print("Returns the string in uppercase",a.upper())

print(a.replace("Hello", "Python"))

print(a.split(" ")) # returns ['Hello', ' World!']

lang="Python_is_a_language"
print(lang.split("_"))



str2 = "a12378awe"

# Calling function
print("To check if String is alphanumeric",str2.isalnum())

print("To check if string contains only alphabets",str2.isalpha())






