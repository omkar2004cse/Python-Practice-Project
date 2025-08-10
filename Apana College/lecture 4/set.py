# set 
s={1,2,3,4,2,3,4,1,3,4} #set can display only single element not occurance of element
print(s)
print("Type of s is:-",type(s))
# empty set
se={ } # python is consider as the dictionary
se=set()
print("type of set is:-",type(se))
print("Length of set is:-",len(se))

# add(element)  these is used to add new element in set
# print(se.add(1))  #none
se.add(1)
print("used the add function:-",se)

# remove(element) these is remove element from the set
# print("remove method:-",s.remove(2))  # none
s.remove(2)
print("remove method:-",s)

# clear() these function is remove all the element from set
s.clear()
print("clear function:-",s)

