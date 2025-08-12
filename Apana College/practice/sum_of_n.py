# WAP to find the sum of frist n number (using while)
n=int(input("Enter a Last Number:-"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("sum of",n,"number is:-",sum)