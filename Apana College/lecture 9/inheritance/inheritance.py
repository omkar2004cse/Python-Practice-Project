# Inheritance property
class car:
    @staticmethod
    def start():
        print("Car is Started")
    @staticmethod
    def stop():
        print("Car is Stoped")
    
    def color(self):
        print("Car colour is Black")

class maruti(car):
    def __init__(self,name):
        self.name=name
        print("This is Maruti Car")
    
    def avg(self):
        print("AVG is 32.33km/hr")

        
# Inheritance
c=maruti("Wagnor")
print(c.name)
print(c.start())
c.color() #Inheritance 
c.avg()
# class access
c1=car()
print(c1.start())