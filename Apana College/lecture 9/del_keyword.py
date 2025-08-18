# del Keyword is used for deleting the object created for the class
class data:
    college_name="JJMCOE"
    def __init__(self,name,roll):
       self.name=name
       self.roll=roll
       print("new data is added")
    
o=data("omkar",14)
print(o.name) #object attribute
print(data.college_name) #class attribute by class name
print(o.college_name) #class attribute access by object
# delete the object
del o.name
# print(o.name) #name attribute is deleted
print(o.roll)
del o #object is deleted
print(o.roll)