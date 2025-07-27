# String is sequence of character. It is also Data type.
print("String is sequence of character. It is also Data type.")

# operation on String 
# Concatination of sting
str1="Hello"
str2="World"
print("Concatination of String:-",str1+str2)

# len (variable_name):- len is Function that is used to calculate the length of string
print("length of ",str1+str2,"is:-",len(str1+str2))

# indexing of String (indexing starting with 0 and end with (n-1))
# empty space (_) is also give number in indexing
str=" I am Python Developer specialization in Django"
print(str[10])
print("length os str is:-",len(str))
# manuplation and modification of string not support (str[10]=t)

# Slicing of String (Accesing part of String)
# str[starting_index : ending_index]
print("Slicing of string is str[1:12]:-",str[1:12])
# str[ :ending_index] start with 0
print("string str[:20]",str[:20])
# str[start_index:] end with length of string [len(str)]
print("String str[5:]:-",str[5:])