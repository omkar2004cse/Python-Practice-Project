# Weight conversion
weight=float(input("Enter your Weight:-"))
unit=input("Enter your weight unit(kilogram for Kg or Pounds for Lbs):-")
if unit=="kg":
    print("weight in pound is:-",round(weight*2.205, 2),"Lbs")
elif unit=='Lbs':
    print("Weight in Kg is:-",round(weight/2.205,2),"Kg")
else:
    print(unit,"is Not Valid")