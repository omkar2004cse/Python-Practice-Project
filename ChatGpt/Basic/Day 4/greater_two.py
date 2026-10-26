# Write a program to find the greater of two numbers.
num1=int(input("Enter a Frist Number:-"))
num2=int(input("Enter a Second Number:-"))
if num1==num2:
    print("Two Numbers are Equal")
elif num1>num2:
    print(num1,"is Greater than",num2)
else:
    print(num2,"is Greater than",num1)