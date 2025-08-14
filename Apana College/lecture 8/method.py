# Method in class
class data:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        print("Data is updated")

    def welcome(self):
        print("welcome",self.name)

s1=data("omkar",93)
print("Parameterized constructor is:",s1.name,s1.mark)
s1.welcome()
