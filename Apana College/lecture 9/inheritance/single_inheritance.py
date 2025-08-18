# Single Inheritance 
class college:
    def c_name(self):
        print("College Name is:- Dr. J. J. Magdum College of Engineering, Jaysingpur")
        self.__address()
    
    def __address(self):
        print("Address is Shriol Road Jaysingpur-416101")
    
class stu1(college):
    def __init__(self,name):
        self.name=name


s1=stu1("omkar")
print(s1.name) #object attribute
s1.c_name()  
# s1.__address() #This is private method