# Private attribute and method
class data:
    def __init__(self,name):
        self.__name=name

    def private_access(self):
        print(self.__name)
        # self.hell()

    def __call(self):
        print("Private Access")

    def hell(self):
        # self.surname=surname
        print("Hello..!")
        self.__call()
        
    

o=data("omkar")
# print(o.__name) #private attribute
print(o.private_access())
o.hell()
# o.__cal()     #private method 