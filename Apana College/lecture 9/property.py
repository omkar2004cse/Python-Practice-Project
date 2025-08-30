# property is decorator
class omkar:
    def __init__(self,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        # percentage=(sub1+sub2+sub3)/3
        # self.percentage=percentage
    @property
    def percentage(self):
        return (self.sub1+self.sub2+self.sub3)/3
o=omkar(45,67,89)
print(o.percentage)
# o.sub2=90
# print(o.percentage) 
# it will not change percentage because percentage is not updated automatically when we change any subject marks
# to solve this problem we use property decorator 
o.sub2=90
print(o.percentage)