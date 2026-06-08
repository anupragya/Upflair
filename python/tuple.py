#TUPLE: 
#heterogeneous collection of data
#immutable: cannot be changed after creation
#ordered: maintains the order of elements
#allows duplicates: can contain duplicate elements


my_tuple= (1, 2, 3, 3, 2, "hello", 4.5)
print(my_tuple)

print("type of data is ", type(my_tuple))
print("length of my tuple is ", len(my_tuple))

print("INDEXING", "\n",my_tuple[0], sep="")
print(my_tuple[1])
print(my_tuple[-1]) #accessing the last element of the tuple
print(my_tuple[4])

print("SLICING\n", my_tuple[2:4], sep="")
#Python automatically separates them with a space. The sep parameter allows us to customize this separator. Instead of always using a space, one can define your own character (like -, @, |, etc.). This makes it very useful for formatting outputs in a clean and readable way.
print(my_tuple[:-1])
print(my_tuple[::2]) #it skips over every second element of the tuple, resulting in (1, 3, 2, 4.5)
print(my_tuple[::-1]) #it reverses the order of the elements in the tuple, resulting in (4.5, 'hello', 2, 3, 3, 2, 1)

#returns the number of times the value 3 appears in the tuple, which is 2 in this case.
print(my_tuple.count(3))
# print(my_tuple.count()) 

#returns the index of the first occurrence of the value "hello" in the tuple, which is 5 in this case.
print(my_tuple.index("hello"))

#TUPLE UNPACKING
a, b, c=(1, 2, 3)
print(a)
print(b)
print(c)

y= 1,5,6,3,2.4,6,7,4,6 #by default it is a tuple because of the comma, even without parentheses
print(type(y))

# to add elements we need typecasting to list and then back to tuple

print("TYPECASTING:")
print(type(y))
lst= list(y) #typecasting to list
print("after typecasting:", type(lst))
lst.append(8) #adding an element to the list

print("list after element was added:", lst)

print("typecasting back to tuple:")
y= tuple(lst) #typecasting back to tuple
print(type(y))
print("tuple after element was added:", y)

print("hello" in my_tuple) #returns True if the substring "hello" is found in the tuple my_tuple, otherwise False
print("world" in my_tuple) #returns True if the substring "world" is found





