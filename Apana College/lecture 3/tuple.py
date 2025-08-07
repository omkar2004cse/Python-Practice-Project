# Tuple 
tup=(122,32,45,'dsf',23,23.543,4j+4,True,23)
print("Tuple can store all the data type element:-",tup)
print(type(tup))
print("length of Tuple is:-",len(tup))

# indexing and slicing support
# They not support for mutable (it is Immutable)
print("indexing :-",tup[3])
print("Slicing:-",tup[2:5])

# Tuple method are
print("index function:-",tup.index(45))
print("count function:-",tup.count(23))
#2d tuple
t=((1,3,4),(2,4,5),(23,45,32))
print(t[1][1])