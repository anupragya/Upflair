#OPERATORS in python: to perform operations on two numbers
#aritmetic operators: addition, sub, mul, div, modulus, exponentiation, floor division
a = 10
b = 3
print("aritmetic operators:")
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

#assignment operators: to assign values to variables
x = 10
print("assignment operators:")
x += 5
print(x)   # 15

x -= 2
print(x)   # 13

x *= 2
print(x)   # 26

print("comparison operators: to compare two values")
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= 10) # True
print(x <= 5)  # False

print("Logical Operators: Used to combine conditions.")
a = 10
b = 20

print(a > 5 and b > 15)   # True
print(a > 15 or b > 15)   # True
print(not(a > 5))         # False

print("Identity operators: Check whether two variables refer to the same object.")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True
print(x is z)      # False
print(x == z)      # True

print("Membership Operators: Check whether a value exists in a sequence.")
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)      # True
print("grapes" not in fruits)  # True