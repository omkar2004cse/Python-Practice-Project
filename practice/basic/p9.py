# find the greatest of between 3 number 
print("Enter a three number:");
num1=int(input("1st number="));
num2=int(input("2nd number="));
num3=int(input("3rd number="));
if(num1>num2):
    if(num1>num3):
        print(num1,"is greater than",num2,"&",num3);
    else:
        print(num3,"is greater than",num1,"&",num2);
else:
    if(num2>num3):
        print(num2,"is greater than",num1,"&",num3);
    else:
        print(num3,"is greater than",num2,"&",num1);