# WAP to find factorial of frist n numbers(using for)
n=int(input("Enter a Last Number:-"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial of",n,"is:-",fact)