# class method 
class omkar:
    name="jadhav"
    @classmethod
    def class_m(cls,name):
        print(name)
        cls.name=name
        

# without object creation

omkar.class_m("omkar")

# object through
print(omkar.name)
obj=omkar()
obj.class_m("king")
print(omkar.name)
print(obj.name)