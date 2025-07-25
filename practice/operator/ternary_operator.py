# ternary operator for finding maximum and minimum number between 3 number
a,b,c=int(input("Enter a=")),int(input("b=")),int(input("c="))

min=a if a<b and a<c else b if b<c else c
print("minimum between",a,b,c,"is:-",min)
max=a if a>b and a>c else b if b>c else c
print("Maximum between",a,b,c,"is:-",max) 