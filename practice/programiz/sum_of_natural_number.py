n=int(input("Enter a Number:-"))
sum=0
if n<0:
    print("Enter a Positive Number")
else:
    # sum=int((n*(n+1))/2)
    # print("Sum of number is:-",sum)
    # OR
    while(n>0):
        sum+=n
        n-=1
    print("Sum is:-",sum)