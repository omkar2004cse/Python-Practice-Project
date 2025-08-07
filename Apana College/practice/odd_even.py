# input from user and check number is odd or even
num=int(input("Enter a number:-"))
if(num==0):
    print(num,"is Zero")
elif(num%2==0):
    print(num,"is Even")
else:
    print(num,"is Odd")