# function
def sum(a1,a2):  #function definition and parameters
    s=a1+a2
    return s  #return value or data of operation is performed

a=int(input("Enter a Frist Number:-"))
b=int(input("Enter a Second Number:-"))
s=sum(a,b) #function call and argument
print("sum of",a,"and",b,"is:-",s)

p=sum(13,42)
print("sum is:-",p)