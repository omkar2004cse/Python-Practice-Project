n=int(input("Enter a Nth number:-"))
print("Odd Number between 1 to",n,'is:-')
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")