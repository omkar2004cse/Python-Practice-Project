num=int(input("Wellcome in Prime Number Cheaker\nEnter a number:-"))
if num==0 and num==1:
    print(num,"is not prime")
elif num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not prime number")
            break
        else:
            print(num,"is prime number")
            break