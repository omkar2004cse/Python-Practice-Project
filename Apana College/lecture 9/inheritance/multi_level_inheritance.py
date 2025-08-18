# Multi-level Inheritance
class college:
    def college_n(self):
        print("Dr. J. J. Magdum College of Engineering, Jaysingpur")

class cse(college):
    def branch(self):
        print("welcome in Computer Science and Engineering Department")

class student1(cse):
    def __init__(self,name):
        self.name=name
        print(name)

s1=student1("omkar") 
print(s1.branch())        
print(s1.college_n())