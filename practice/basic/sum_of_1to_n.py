# Calculate sum of all numbers from 1 to a given number
last=int(input("Enter a last number upto calculate total is:-"))
sum=0
for x in range(1,last+1):
    sum=sum+x
print("Sum of from",1,"to",(last),"is:-",sum)