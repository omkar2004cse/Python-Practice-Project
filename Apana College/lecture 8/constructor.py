# constructor 
class student:
    college="JJMCOE"
    # default constructor
    def __init__(self):
        print("jay shree ram")                     

    # parameterized constructor
    def __init__(self,roll,mark):
        self.roll=roll
        self.mark=mark
        print("New Data Added")
    
s1=student(14,90)
print(s1.college,s1.roll,s1.mark)

s2=student(15,90)
print(student.college,s2.roll,s2.mark)