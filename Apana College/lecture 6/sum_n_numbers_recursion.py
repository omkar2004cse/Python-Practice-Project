# write a recursive function to calculate the sum of frist n natural numbers
def sum(p):
    if(p==0):
        return 0
    return p+ sum(p-1)


n=int(input("Enter a Nth Number:-"))
print("sum of",n,"is:-",sum(n))