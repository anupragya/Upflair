print("hello python")
age=21
print(age)
# variable declaration rules:
# 1. variable name should start with a letter or underscore
# 2. variable name can contain letters, numbers and underscores
# 3. variable name should not be a reserved keyword
# 4. variable name should be meaningful and descriptive

#DATA TYPES
# 1. int: whole numbers
# 2. str: sequence of character inside ""
name = "Anupragya Chaudhary"
print("my name is ", name)
print("type of data ", type(name))
print("length of my string ", len(name))
print("INDEXING")
print(name[0])
print(name[1])
print(name[2])
print(name[3])


print("SLICING")
print(name[0:2])
print(name[1:])
print(name[:3])
print(name[:])
print(name[::-1]) #reverses the string  

upper_case= name.upper() #converts to uppercase
print(upper_case)
lower_case= name.lower() #converts to lowercase
print(lower_case)

name1="ANUpragya"
case_fold= name1.casefold() #converts to lowercase and removes any special characters
print(case_fold)


#The main difference is that str.capitalize() targets only the first character of the entire string, while str.title() targets the first character of every single word
print(name.capitalize()) #capitalizes the first letter of the string
print(name.title()) #capitalizes the first letter of each word in the string

print(name.index("n")) #returns the index of the first occurrence of a substring in the string, raises ValueError if not found
print(name1.count("a")) #counts the number of occurrences 
print(name.find("s")) #returns the index of the first occurrence of a substring in the string, returns -1 if not found
print(name.replace("o", "a")) #replaces all occurrences of a substring with another 


greet="hi anand"
print(greet.replace("hi", "hello"))


rollno= "  018  "

print(rollno.isdigit()) #returns True if all characters in the string are digits, otherwise False

print(name1.isalpha()) #returns True if all characters in the string are alphabetic

print(name1.isalnum()) #returns True if all characters in the string are alphanumeric (letters and numbers), otherwise False

print(name.split()) #splits the string into a list of substrings based on whitespace

print(name.split("a")) #splits the string into a list of substrings based on given condition "a"
print(rollno.strip()) #removes leading and trailing whitespace from the string
print(rollno.lstrip()) #removes leading whitespace from the string
print(rollno.rstrip()) #removes trailing whitespace from the string


#intro= '''Hello everyone, I'm {name}, an engineering student with a passion for both technology and literature. I believe in continuous learning, effective communication, and turning ideas into meaningful experiences. My goal is to grow as a professional while never losing my love for creativity and storytelling.'''
#print(intro)

#FORMATTING OF STRING

address= "Agra"
print(f"""Hello everyone, I'm {name}, an engineering student with a passion for both technology and literature. I am from {address}. My rollno is {rollno}. I believe in continuous learning, effective communication, and turning ideas into meaningful experiences. My goal is to grow as a professional while never losing my love for creativity and storytelling.""")
#f-string is a way to format strings in Python, it allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the __format__ protocol. F-strings are prefixed with 'f' or 'F' before the opening quotation mark.

path = r"C:\Users\anupr\upflair" #raw string to avoid escape characters
print(path)
import os
print(os.listdir(path)) # lists all the files and directories in the specified path

college_name= "Anand Engineering College"
college_address="Kanota"
#print(college_name* college address) #repeats the string college_name by the number of times specified by college_address, which is not a valid operation and will raise an error

print(college_name*3) #repeats the string college_name 3 times, resulting in "anand engineering collegeanand engineering collegeanand engineering college"

print("college_name" + "college_address") #concatenates the two strings, resulting in "college_namecollege_address"

print(college_name + " " + college_address) #concatenates the two strings with a space in between, resulting in "anand engineering college Kanota"

print("An" in college_name) #returns True if the substring "An" is found in the string college_name, otherwise False

print("an" in college_name) #returns True if the substring "an" is found in the string college_name, otherwise False



