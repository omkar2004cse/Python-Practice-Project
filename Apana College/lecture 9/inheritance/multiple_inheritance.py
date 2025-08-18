# Multiple inheritance 
class college:
    c_name="Dr. J. J. Magdum College of Engineering, Jaysingpur"
    def code(self):
        print("college code is:-6277")

class cse(college):
    dept_cse="Department of Computer Science and Engineering"
    def place(self):
        print("35 Student of Computer Science and Engineering are Placed")

class it(college):
    dept_it="Department of Information Technology"
    def n_place(self):
        print("50 Student of Information Technology not placed")

class cs_it(cse,it):
    def __init__(self,name):
        print("This is CSE and IT Depatment")
        self.name=name

s1=cs_it("omkar")
s1.place()
print(s1.dept_cse)

print(s1.dept_it)
s1.n_place()