n1=int(input("Enter a Frist number is:-"))
n2=int(input("Enter a Second number is:-"))
n3=int(input("Enter a Thrid number is:-"))
if n1<n2:
    if n1<n3:
        print(n1,"is Smaller than",n2,"and",n3)
    else:
        print(n3,"is Smaller than",n1,"and",n2)
else:
    if n2<n3:
        print(n2,"is Smaller than",n1,"and",n3)
    else:
        print(n3,"is Smaller than",n1,"and",n2)
