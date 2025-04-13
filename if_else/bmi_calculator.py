print("Welcome in BMI Calculator")
weight=float(input("Enter your weight in kg is:-"))
height=float(input("Enter your height in meter is:-"))
bmi=weight/(height**2)
print("Your BMI is:-",bmi)
if(bmi<=18.5):
    print("you are Underweight")
elif(bmi<=25):
    print("You have normal weight")
elif bmi<=30:
    print("You are OverWeight")
else:
    print("You are Obese")