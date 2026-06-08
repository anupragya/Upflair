#QUESTION 1
from turtle import update


s="Hello, World"
print("the first character is:", s[0])
print("the last character is:", s[-1])
print("the length of the string is:", len(s))
print("Convert the string to uppercase :", s.upper())
print("Convert the string to lowercase :", s.lower())
print("the string in reverse order is:", s[::-1])

#QUESTION 2
print("\nthe first four characters are:", s[0:4])
print("characters from index 2 to 5 are:", s[2:5])
print("the complete string in reverse order is:", s[::-1])

#QUESTION 3
lst=[1, 2, 3, 4, 5]
print("\nAdding an element using append():")
lst.append(6)
print("The updated list is:", lst)

print("Insert an element at a specific position:")
lst.insert(2, 10)
print("The updated list is:", lst)

print("Remove an element using remove() ")
lst.remove(6)
print("The final list is:", lst)

print("Delete the last element using pop()")
lst.pop(-1)
print("The final list is:", lst)

print("Reverse the list", lst[::-1])

lst.sort()
print("Sort the list", lst)

print("the length of the list", len(lst))

print("Count the occurrence of an element ", lst.count(2))

#QUESTION 4
tup=(1,5,6,8,1)
print("\nPrint the first element: ", tup[0])

print("the last element: ", tup[-1])


print("the length of the tuple: ", len(tup))

print("Printing elements using slicing: ", tup[:])

print("the maximum numerical tuple elements: ", max(tup))

print("minimum numerical tuple elements: ", min(tup))

print("sum of numerical tuple elements: ", sum(tup))

#QUESTION 5
#Packing a tuple
a, b, c, d=(1, 2, 3,4)

#Unpacking a tuple
a, b, c, d=(1, 2, 3, 4)
print("\n")
print(a)
print(b)
print(c)
print(d)

#QUESTION 6
student={"name": "ANU",
       "age": 21,
       "course": "BTECH",
       "address": "AGRA"
       }
print("\nPrint all keys: ", student.keys())

print("Print all values:", student.values())

print("Print all items: ", student.items())

print("update the Address: ") 
student.update({"area_of_study": student.pop("course")}) 
print(student)

print("Add a new key called Branch: ")
student["branch"]= "CSE"
print(student)

#QUESTION 7
lst2 = [1, 2, 3, 4, [2, 5], 7]
print("\naccess an element from a nested list: ", lst2[4][1])

#Question 8
print("\n")
t= int(input("enter a number here: "))

print("Add 10 using the += operator: ")
t+=10
print("updated value", t)

#QUESTION 9
print("\nTYPECASTING: ")
num1= input("enter first number: ")
print(type(num1))
num2= input("enter second number: ")
print(type(num2))
nm1= int(num1) #Convert them to integers 
nm2= int(num2)
print(nm1*nm2) #multiply

#QUESTION 10
print("\n")
print(student.get("name")) 
print(student.keys()) 
print(student.values()) 
print(student.items())

#QUESTION 11: Create a copy of a list using copy() and print both the original and copied lists.

ts=[4, 13, 1989, 15, 22]
tay= ts.copy()
print("\n", ts) #prints original list
print(tay) #prints copy of list

