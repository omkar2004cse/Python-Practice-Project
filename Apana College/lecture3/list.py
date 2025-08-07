# list
marks=[70,75,94,99,35,43,34]
print("list are:-",marks)
print("Type is:-",type(marks))
print("length of mark is:-",len(marks))

# list contain different data type values
data=["omkar",21,84.33,4j+5,{1,2,3},(12,13.2),[12,43,55,21],] #store int,str,float,list,complex
print("List can store different values:-",data)
print("type is:-",type(data))

# Indexing support in list
# slicing support in list 
# list is mutable
marks[2]=23
print("Indexing and mutable is supported in list:-",marks)
print("List support slicing:-",marks[2:])

# 2d list access 
li=[[1,2,3],[4,5,6],[7,8,9]]
print("2d list element access",li[2][2])
for i in range(3):
    for j in range(3):
        print(li[i][j])
    print("/")

# list convert into Tuple
tup=tuple(marks)
print("list is convert into Tuple:-",tup)
print("Type is:-",type(tup))
print("Length is:-",len(tup))