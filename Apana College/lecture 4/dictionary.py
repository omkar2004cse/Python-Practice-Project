# Dictionary Data type
d={"name":"omkar","roll":14,"CGPA":8.3}
print(d["CGPA"])
d["CGPA"]=8.4
print("Dictionary is:-",d)
print("Type:-",type(d))
print("Length is:-",len(d)) 

# Nested Dictionary
student={
    "name":"omkar",
    "Roll":14,
    "subject":{
        "python":"done in 2 days",
        "web developement":"done in upto november",
        "data science":"done before new year 2026"
    }
}
print("Dictionary is:-",student)
print("add cgpa in student")
student["cgpa"]=8.4 # added new key and value in dictionary
print(student)
print(student["subject"])
print("type of subject is:",type(student["subject"]))
print("value from the nested dectionary:-",student["subject"]["data science"])