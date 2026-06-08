#LIST
my_list= [1, 2, 2, 3, 4, "hello"]
#mutable, ordered, allows duplicates, indexed, hetrogeneous
#there are nested lists also 

print(my_list)
print(type(my_list))
print(len(my_list))
print(my_list[0]) #accessing the first element of the list
print(my_list[5]) #accessing the sixth element of the list 

#print(my_list.append(100))
lst= my_list.append(100) #appends the element 100 to the end of the list, modifies the original list and returns None
print(my_list)
print(lst) #prints None because the append method returns None  

my_list.extend([2, 3, 6, 8])
print(my_list)

lst1=[500, 60, 49,  3, 6, 12]
print(lst1 + my_list)

my_list.pop()
print(my_list) #removes and returns the last element of the list, modifies the original list
my_list.pop(2)
print(my_list) #removes and returns the element at index 2 of the list, modifies the original list


my_list.remove("hello")
print(my_list)

print(my_list.count(2)) #returns the number of occurrences of the element 2 in the list

lst1.reverse() #reverses the order of the elements in the list, modifies the original list and returns None
print(lst1) #prints None because the reverse method returns None

print(lst1.sort()) #sorts the elements of the list in ascending order, modifies the original list and returns None
print(lst1) #prints None because the sort method returns None

#print(lst1[4][2]) #accessing the third element of the fifth element of the list lst1, which is a nested list

lst2= [1, 2, 3, 4, 5, 6]

print(lst1+lst2)
# print(lst1*lst2)
# print(lst1-lst2) #unsupported operand type(s) for -: 'list' and 'list'
# print(lst1/lst2) #unsupported operand type(s) for /: 'list'
print(lst2*3) #repeats the list lst2 3 times, resulting in [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]


