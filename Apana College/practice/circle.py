# define circle class with area and parameter methods 
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        print(3.14*self.r*self.r)
    def parameter(self):
        print(2*3.14*self.r)

c1=circle(5)
c1.area()
c1.parameter()
c2=circle(10)  
c2.area()
c2.parameter()