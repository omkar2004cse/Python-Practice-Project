# Static Method
class data:
    @staticmethod
    def store(name):
        print("Static method:-",name)

o=data()
o.store("omkar")

# witout object creation
data.store("don")