#SETS
#duplicate items will be printed once, mutable, heterogenous, add and remove value, UNORDERED

ts={"red", 13, 1989, "midnights", 13, "folklore"}
print("the data type is ", type(ts))
print("this is my set ", ts)

ts.add(100) #to add in elements
ts.remove(1989) #to remove the elements, if element is not in it returns error
ts.discard(1334)# will not return error if the element is not present in it
print(ts)
#INDEXING and SLICING can not be performed since there is no order in sets
#print(ts[1]) will give TYPEERROR

#set operations
a={2,3,4,5,6,7,8,9}
b={2,4,6,8}
c={3,6,9}
print(c.issubset(a))
print(b.union(c))
print(c.intersection(a))
print(b.update(c))
print(b)

#if we have a list with many duplicate values, and to simply remove it we can do typecasting
y=[1,1,1,3,4,5,5,5,6,7,8,9,2,4,5,6,7,9]
print("TYPECASTING:")
print(type(y))
st= set(y) #typecasting to set
print("after typecasting:", type(st))


print("set is:", st)

print("typecasting back to list:")
y= list(st) #typecasting back to list
print(type(y))
print("list after duplicates were removed: ", y)

print(13 in ts)

