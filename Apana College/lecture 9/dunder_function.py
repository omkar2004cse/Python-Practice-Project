# Dunder function 
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(f"{self.real}+{self.img}i")

    def __add__(self,num2):
        return complex(self.real+num2.real,self.img+num2.img)

o=complex(1,3)
o.show()
o2=complex(4,5)
o2.show() 
o3=o+o2
o3.show()