# check eligible for vote or not
age=int(input("Enter a your age:-"))
if(age>=18):
    print("You are Eligible for Vote")
else:
    print("You are Not Eligible for Vote.\nWait",(18-age),"Year to eligible to Vote")