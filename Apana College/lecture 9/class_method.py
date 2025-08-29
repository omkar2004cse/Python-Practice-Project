# class method 
class omkar:
    @classmethod
    def class_m(cls,name):
        print(name)

# without object creation

omkar.class_m("omkar")

# object through
obj=omkar()
obj.class_m("king")