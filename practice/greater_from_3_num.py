n1=int(input("Enter a Frist number is:-"))
n2=int(input("Enter a Second number is:-"))
n3=int(input("Enter a Thrid number is:-"))
if n1>n2:
    if n1>n3:
        print(n1,"is greater than",n2,"and",n3)
    else:
        print(n3,"is greater than",n1,"and",n2)
else:
    if n2>n3:
        print(n2,"is greater than",n1,"and",n3)
    else:
        print(n3,"is greater than",n1,"and",n2)
