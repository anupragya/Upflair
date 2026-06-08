#QUESTION 1
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
a, b, c, d=(1, 2, 3)

#Unpacking a tuple
a, b, c, d=(1, 2, 3, 4)
print("\n")
print(a)
print(b)
print(c)
print(d)
