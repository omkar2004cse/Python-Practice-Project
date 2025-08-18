# Super method 
class car:
    def __init__(self,type):
        self.type=type
        print("Type is:-",type)
    def avg(self):
        print("Average is 23km")
    speed="43 Km/Hr"

class maruti(car):
    def __init__(self,name,type):
        self.name=name
        print(name)
        super().__init__(type)  #super method through value pass kale
        # print(speed)
        print(super().speed) #super method through attribute access kele
        super().avg()  #super method through parent che function access kele
        
c1=maruti("Wagnor","petrol")
