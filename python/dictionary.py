#DICTIONARY
#mutable: can be changed after creation
#unordered: does not maintain the order of elements
#key-value pairs: each element is a key-value pair
#keys must be unique and immutable
#values can be of any type and can be duplicated

student={"name": "Anupragya",
         "age":21,
         "branch":"CSE",
         "roll_no": "23cs018",
         "address": "Agra"
         }
print(student)
print("type of data is:",type(student))
print("length of dictionary is:", len(student))
print(student["name"]) #accessing the value of the key "name" in the dictionary student
print(student['age']) #accessing the value of the key "age" in the dictionary

student["age"]=20 #modifying the value of the key "age" in the dictionary student
print(student)

print(student.get("branch")) #returns the value of the key "branch" in the dictionary student, which is "CSE" in this case
print(student.get("name"))

print(student.keys()) #returns a view object that displays a list of all the keys in the dictionary student
print(student.values()) #returns a view object that displays a list of all the values in the dictionary student
print(student.items()) #returns a view object that displays a list of all the key-value pairs in the dictionary student

student["cgpa"]=10 # to add some key value pair
print(student)

students={ "names": ["Pratibha", "Sanskriti", "Aditi"],
          "rollno": [1, 2, 3],
          "address": ["agra", "jaipur", "xyz"]
          }

print(students)
#deepcopy and update and copy()

print("to change name of key:")
student.update({"area_of_study": student.pop("branch")}) #In Python, update() is a built-in method primarily used to modify dictionaries or sets in-place 
print(student)

#to take input from the user
dict1= {"age": input("enter your age: "),
        "name": input("enter your name: ")
       }
print(dict1)

a = input("enter the address:")
dict2 ={"address": a}
print(dict2)

#shallow copy vs deep copy
import copy

a = [[1, 2, 3], [4, 5, 6]]

# Creating a deep copy of the nested list 'a'
b = copy.deepcopy(a)

# Modifying an element in the deep-copied list
b[0][0] = 99 
print("b: ", b) 
print("a: ", a)

import copy  

a = [[1, 2, 3], [4, 5, 6]]

# Creating a shallow copy of the nested list 'original'
b = copy.copy(a)

# Modifying an element in the shallow-copied list
b[0][0] = 99

# Printing the original and shallow-copied lists  
print("b: ", b) 
print("a: ", a)







