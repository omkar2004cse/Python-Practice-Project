number=int(input("Enter a Number to Calculate its Factorial:-"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print("Factorial of",number,"is:-",factorial)