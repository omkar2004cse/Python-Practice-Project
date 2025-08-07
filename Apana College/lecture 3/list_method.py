# List Method aor Function
li=[13,42,52,1,45,75,4,68]
print("Type is:-",type(li))
print("Length is:-",len(li))
# append(element)  add new element at the end of list
print(li.append(12)) # None
print("Append Function:-",li)

# sort() sort the list in accending from
li.sort()
print("Sort function:-",li)
# decending order using sort function
li.sort(reverse=True)
print(li)

# reverse()  these function reverse the element of list 
li.reverse()
print("Reverse function:-",li)

# insert(index,element)  these function used to add new element at particular index
li.insert(2,43)
print("insert function:-",li)

# remove(element) these remove the element frist occurence in list
li.remove(42)
print("Remove Function:-",li)

# pop(index)   remove element list from particular index
li.pop(3)
print("pop function:-",li)

