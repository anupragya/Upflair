#file handling (write and read students)
file = open("student.txt", "w")

name = input("Enter student name: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

file = open("student.txt", "r")

print("\nFile Content:")
print(file.read())

file.close()