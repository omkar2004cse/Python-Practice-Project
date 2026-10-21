# Write a program to swap two variables.
num1=int(input("Enter a Frist Number:-"))
num2=int(input("Enter a Second Number:-"))
print("Before Swapping \nn1:-",num1,'\t','n2:-',num2)
# temp=num1
# num1=num2
# num2=temp
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After Swapping \nn1:-",num1,'\t','n2:-',num2)