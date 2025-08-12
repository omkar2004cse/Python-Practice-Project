# WAF to find the Factorial of n

def fact(p):
    f=1
    for i in range(1,p+1):
        f*=i
    print("Factorial of",p,"is:-",f)

n=int(input("Enter a Number is:-"))
fact(n)