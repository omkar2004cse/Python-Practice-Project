# Recursion  
# function calling itself
def num(n):
    if(n==0):
        return
    print(n)
    num(n-1)

n=int(input("Enter Nth Number:-"))
num(n)

# factorial by recursion
def fact(p):
    if(p==0):
        return 1
    else:
        return p*fact(p-1)
num=int(input("enter a Nth number:-"))
print(fact(num))