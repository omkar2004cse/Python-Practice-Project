# Static method
class data:
    college="JJMCOE" #class attribute
    def __init__(self,name,age):
        self.name=name  #object attribute
        self.age=age
    #method
    def print(self):
        print("Hi...",self.name,"\nyour age is:-",self.age)
    @staticmethod #decorator
    def hello():
        print("Hi Coder..")

o=data("omkar",21)
o.print() #method
o.hello() #static method