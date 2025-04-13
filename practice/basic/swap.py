print("Performing Swaping Two Number")
a=int(input("Enter a value of a:-"))
b=int(input("Enter a value of b:-"))
# temp=a
# a=b
# b=temp
a=a+b
b=a-b
a=a-b
print("Swaping is performed \na=",a,id(a),"\nb=",b,id(b))