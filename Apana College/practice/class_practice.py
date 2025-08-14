# create student class that takes name & marks of 3 subjects as argument in constructor .then create a method to print the average
class student:
    def __init__(self,name,s1,s2,s3):
        self.name=name
        self.s1=s1
        self.s2=s2
        self.s3=s3

    def avg(self):
        a=(self.s1+self.s2+self.s3)/3
        # return a
        print(self.name,"you get:-",a,"%")

n=input("Enter your name:-")
s1=int(input("Enter subject 1 mark:-"))
s2=int(input("Enter subject 2 mark:-"))
s3=int(input("Enter subject 3 mark:-"))

o1=student(n,s1,s2,s3)
# print(n,"you get:-",o1.avg())
o1.avg()