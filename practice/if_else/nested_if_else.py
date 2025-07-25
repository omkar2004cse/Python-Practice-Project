age=int(input("Enter a your Age:-"))
if(age>=18):
    print("You Can Ride")
    weight=int(input("Enter a your Weight in kg is:-"))
    if(weight<=25):
        print("Pay 100Rs")
    elif(weight<=50):
        print("Pay 200Rs")
    else:
        print("pay 300Rs")
else:
    print("Can't Raid")