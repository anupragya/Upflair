#create two objects and display their grades
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"


# Creating two objects
student1 = Student("Rahul", 85)
student2 = Student("Priya", 92)

# Displaying grades
print(student1.name, "Grade:", student1.calculate_grade())
print(student2.name, "Grade:", student2.calculate_grade())