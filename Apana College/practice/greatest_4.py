# Take input from the user four number and find the greatest from them
n1=int(input("Enter a Frist Number:-"))
n2=int(input("Enter a Second Number:-"))
n3=int(input("Enter a Third Number:-"))
n4=int(input("Enter a Fourth Number:-"))
if(n1>n2 and n1>n3 and n1>n4):
    print(n1,"is Greater than",n2,n3,n4)
elif(n2>n1 and n2>n3 and n2>n4):
    print(n2,"is Greater than",n1,n3,n4)
elif(n3>n1 and n3>n2 and n3>n4):
    print(n3,"is Greater than",n1,n2,n4)
else:
    print(n4,"is Greater than",n1,n2,n3)