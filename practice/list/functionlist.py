mark=[12,2,3,10,56,2,99,72,2,4,76,23,15,3,11]
print("print list=",mark)
# length function
print("length of length:-",len(mark))
# count function
print("Calulate the count of 2 in List present:-",mark.count(2))
# index function element cha index print karte
print("index of 99 element:-",mark.index(99))


# append function
# upadate zale pan print hot nahe(None)
print("print None hote:-",mark.append(3))
# 12,2,3,10,56,2,99,72,2,4,76,23,15,3,11,3
# update zale
mark.append(13)
# 12,2,3,10,56,2,99,72,2,4,76,23,15,3,11,3,13
print("Append function(add element in end of list):-",mark)
print("lenght of list is:-",len(mark))
# insert function add element paticular index and update the list 
# do not remove tya index cha element, pan new element add hoto aane length of list increse by one 
print("insert the 33 zala pan print none hote:",mark.insert(7,33)) 
print("insert 33 at index 7",mark)
print("length of list is",len(mark))
# extend is used to add one list in another list
# syntax is:-list_name1.extend(list_name2)
name=["king", "don","Raj"]
print("New list:-",name)
name.extend(mark)
print("extend mark list in name list:-",name)
# remove function


# reverse the list
# mark.reverse()
# print("reverse the string is:-",mark)
# print("Reverse the list order is(reverse function):-",mark)
# # sort function
# mark.sort()
# print("sorted list is:-",mark)
# mark.sort(reverse=True)
# print("Sorted list reverse is:-",mark)
