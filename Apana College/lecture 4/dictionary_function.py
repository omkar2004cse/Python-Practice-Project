# Dictionary function
student={
    "name":"omkar jadhav",
    "roll":59,
    "subject":{
        "marathi":97,
        "hindi":98,
        "english":90,
        "maths":97,
        "science":94
    }
}
print("dictionary is:-",student)
print("Type is:-",type(student))
# keys() these function return the all keys from the dictionary
print("Keys function is:-",student.keys())

# value() these gives all values from the dictionary
print("All values form dictionary is:-",student.values())

# items() these return the key and value pair in from of tuple
print("item function:-",student.items())
# print("Using the item function:-",list(student.items())) # they return pair in from of list

# get("key")  these return the value according to these key
print("value for the specific key is:-",student.get("roll")) 
# print("value of key:-",student.get("city"))  # key present nasel tr none output dete

# update(newdictionary or "key":value)
student["city"]="snagli"
print(student)
n_dict={
    "friends":"god"
}
student.update(n_dict)
print("update the dictionary is:-",student)