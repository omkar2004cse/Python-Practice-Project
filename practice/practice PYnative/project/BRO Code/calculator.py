num1=float(input("Enter a 1st Number="))
num2=float(input("Enter a 2nd Number="))
operation=input("Enter a operator( + , - , * , / , ** , // , % ):-")
if operation=="+":
    result=num1+num2
    print(result)
elif operation=='-':
    result=num1-num2
    print(result)
elif operation == "*":
    result=num1*num2
    print(round(result,2))
elif operation=='/':
    result=num1/num2
    print(round(result, 2))
elif operation=="**":
    print(round(num1 ** num2,2))
elif operation=="//":
    print(round(num1 // num2,2))
elif operation=="%":
    print(round(num1 % num2,2))
else:
    print(operation,"is not Valid")